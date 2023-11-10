import io
import pandas as pd
import matplotlib.pyplot as plt

from datetime import timedelta, datetime
from prophet import Prophet
from django.core.files.images import ImageFile

import seaborn as sns
sns.set_theme(style="darkgrid")


from core.predictions.models import LandingPageUsuarios


def generate_data_frame():
    # Get info from the database
    data = list(LandingPageUsuarios.objects.values('FECHA_INGRESO', 'TOTAL_CLICKS'))

    # Convert to Pandas  DataFrame
    df = pd.DataFrame(data)

    # Rename the columns
    df.columns = ['ds', 'y']
    df['ds'] = pd.to_datetime(df['ds'])
    return df


def generate_forcast(df):
    # Create a Prophet model, Train it and generate the forecast
    model = Prophet(scaling='minmax')
    model.fit(df)

    # future = model.make_future_dataframe(periods=14)
    # Define the number of days you want to forecast into the future
    num_days_to_forecast = 30  # Adjust this according to your needs

    # Specify the start date and end date for the forecast period
    start_date = df['ds'].max()  # Use the latest date in your historical data
    # end date today
    end_date = datetime.today().date() + timedelta(days=30)
    # end_date = start_date + pd.DateOffset(days=num_days_to_forecast)

    # Create a DataFrame with future dates
    # future_dates = pd.date_range(start=start_date, periods=num_days_to_forecast, freq='D')
    future_dates = pd.date_range(start=start_date, end=end_date, freq='D')
    future_df = pd.DataFrame({'ds': future_dates})
    forecast = model.predict(future_df)
    return forecast, start_date, end_date

def generate_graph(instance, df):
    figure = io.BytesIO()
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=df['ds'], y=df['y'])
    plt.ylabel('Visitas a la Landing Page')
    plt.xlabel('Dias')
    plt.title('Conjunto de Datos Historicos')
    # plt.show()
    plt.savefig(figure, format='png')
    instance.image_feed_model.save(f'result-historic-landing-{timedelta(days=7)}.png', ImageFile(figure))
    plt.clf()

def generate_replot(df):
    copy_df = df.copy()
    sns.relplot(
        data=copy_df,
        x="ds", y="y", col="ds",
        hue="ds", style="ds", size="y",
    )
    plt.show()
    plt.clf()

def generate_graph_results(instance, top_10_products):
    figure = io.BytesIO()
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=top_10_products['ds'], y=top_10_products['yhat'])
    # plt.plot(compara2['real']) # blue
    # plt.plot(compara2['prediccion']) # red
    plt.ylabel('Paginas con Click')
    plt.xlabel('Dias')
    plt.title('Predicciones de Visitas a las Paginas del Sitio') 
    plt.savefig(figure, format='png')
    # plt.show()
    instance.image_generated.save(f'result-{timedelta(days=7)}-landing.png', ImageFile(figure))
    plt.clf()


def main_generate_predictible(instance, TODAY, CANT=40):
    """
    Main function to generate the predictions
    Steps:
        - Get data from the database
        - Convert to Pandas DataFrame
        - Create a Prophet model, Train it and generate the forecasting
    """
    START_DATE = TODAY.strftime("%Y-%m-%d")

    """Return a list with many elemns"""
    df = generate_data_frame()

    forecast, start_date, end_date = generate_forcast(df)

    instance.start_date = start_date
    instance.end_date = end_date
    instance.save()


    predicted_demand = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    top_10_products = predicted_demand[forecast.ds > START_DATE]

    final_array = []
    zip_nn = zip(top_10_products['ds'], top_10_products['yhat'], top_10_products['yhat_lower'], top_10_products['yhat_upper'])
    for ds, yhat, low, high in zip_nn:
        final_array.append({
            'most_probable': int(yhat),
            'less_probable_low':  int(low),
            'less_probable_high': int(high),
            'date_predict': ds,
        })

    generate_graph(instance, df)
    generate_graph_results(instance, top_10_products)
    print(final_array)

    return final_array

