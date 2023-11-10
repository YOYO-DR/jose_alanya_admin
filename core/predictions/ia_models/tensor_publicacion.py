'''
https://nbviewer.org/github/jbagnato/machine-learning/blob/master/Series_Temporales_con_RRNN.ipynb
https://www.aprendemachinelearning.com/pronostico-de-series-temporales-con-redes-neuronales-en-python/
https://www.aprendemachinelearning.com/pronostico-de-ventas-redes-neuronales-python-embeddings/
https://towardsdatascience.com/tensorflow-keras-cheat-sheet-5ec99d9a1ccf
https://www.youtube.com/watch?v=qFJeN9V1ZsI
https://ahlemkaabi1412.medium.com/time-series-forecasting-using-keras-tensorflow-3f0e0c902b9b
https://keras.io/examples/timeseries/timeseries_traffic_forecasting/
https://stackoverflow.com/questions/45587378/how-to-get-predicted-values-in-keras
https://stackoverflow.com/questions/76480498/how-to-predict-a-list-of-values-in-keras
'''
import io
from datetime import timedelta
from prophet import Prophet

import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras import layers, models, optimizers, metrics
from sklearn.preprocessing import MinMaxScaler

from django.core.files.images import ImageFile

# Plots
# ==============================================================================
import matplotlib.pyplot as plt


from core.predictions.models import PresupuestoServicios, Servicios, PresupuestoDetallesServicios, PublicacionesFacebook


FILE_NAME_INTERACCIONES = './tensor_data/interacciones.csv'

PASOS=7

# training parameters
EPOCHS = 40 # 40

def generate_cvs_publicaciones(FILE_NAME=FILE_NAME_INTERACCIONES):
    data = PublicacionesFacebook.objects.exclude(comentarios=0).values('id_publicacion', 'comentarios')
    # data = PublicacionesFacebook.objects.values('id_publicacion', 'comentarios')
    data = list(data) + list(data) + list(data) + list(data) + list(data)

    # Create a DataFrame
    df = pd.DataFrame(data)

    print(df.head())

    # save df to csv
    df.to_csv(FILE_NAME, index=False, header=False)

    return FILE_NAME


def read_cvs_and_generate_data_frame(FILE_NAME):
    df = pd.read_csv(FILE_NAME,  parse_dates=[0], header=None, index_col=0, names=['ds','y'])
    return df


# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg

def preparate_keras_data(df):
    values = df.values

    # ensure all data is float
    values = values.astype('float32')

    scaler = MinMaxScaler(feature_range=(-1, 1))
    values=values.reshape(-1, 1)
    scaled = scaler.fit_transform(values)

    # frame as supervised learning
    reframed = series_to_supervised(scaled, PASOS, 1)

    return reframed, scaler


def split_train_test_set(reframed, num_rows):
    # split into train and test sets
    values = reframed.values
    # n_train_days = 315 + 289 - (30 + PASOS)
    n_train_days = int(num_rows / 2)
    train = values[:n_train_days, :]
    test = values[n_train_days:, :]
    print(test.shape)
    # split into input and outputs
    x_train, y_train = train[:, :-1], train[:, -1]
    x_val, y_val = test[:, :-1], test[:, -1]
    # reshape input to be 3D [samples, timesteps, features]
    x_train = x_train.reshape((x_train.shape[0], 1, x_train.shape[1]))
    x_val = x_val.reshape((x_val.shape[0], 1, x_val.shape[1]))
    return x_train, y_train, x_val, y_val

# Create a normal network Feedforward
def make_model_keras():
    # Return a keras model with three layers
    model = models.Sequential() 
    model.add(layers.Dense(PASOS, input_shape=(1, PASOS), activation='tanh'))
    model.add(layers.Flatten())
    model.add(layers.Dense(1, activation='tanh'))
    model.compile(loss='mean_absolute_error', optimizer='Adam', metrics=["mse"])
    model.summary()
    return model


def train_model(model, x_train, y_train, x_val, y_val):
    # Train model and check with validation data
    model.fit(x_train, y_train, epochs=EPOCHS, batch_size=10, verbose=2, validation_data=(x_val, y_val))
    return model


def show_results_accuracy(instance, results, y_val, x_val):
    figure = io.BytesIO()
    plt.figure(figsize=(12, 8))

    plt.scatter(range(len(y_val)),y_val,c='g')
    plt.scatter(range(len(results)),results,c='r')
    plt.ylabel('Tensorflow valores')
    plt.xlabel('Id de Servicios')

    plt.title('Validar la precisión del modelo de Tensorflow (valores-verdes) (resultados-rojos)')
    # plt.show()
    plt.savefig(figure, format='png')
    content_file = ImageFile(figure)
    # add image file name
    name_file = f'Validate-{timedelta(days=7)}.png'
    instance.image_validate_model.save(name_file, content_file)
    plt.clf()

def show_history_loss(history):
    plt.plot(history.history['loss'])
    plt.title('loss')
    plt.plot(history.history['val_loss'])
    plt.ylabel('Tensorflow valores')
    plt.xlabel('Ids de Servicios')
    plt.title('Perdida de Validacion')
    plt.clf()


def comparate_results(instance, scaler, results, y_val):
    compara = pd.DataFrame(np.array([y_val, [x[0] for x in results]])).transpose()
    compara.columns = ['real', 'prediccion']

    inverted = scaler.inverse_transform(compara.values)

    compara2 = pd.DataFrame(inverted)
    compara2.columns = ['real', 'prediccion']
    compara2['diferencia'] = compara2['real'] - compara2['prediccion']
    # print(compara2.head())

    # Generate image
    figure = io.BytesIO()
    plt.figure(figsize=(12, 8))
    plt.plot(compara2['real']) # blue
    plt.plot(compara2['prediccion']) # red
    plt.ylabel('Id de Servicios')
    plt.xlabel('Dias')
    plt.title('Comparación resultada del modelo entrenado de Tensorflow (real-azul) (valor predecido-naranja)')
    plt.savefig(figure, format='png')
    # plt.show()
    instance.image_compare_results.save(f'compare-{timedelta(days=7)}.png', ImageFile(figure))
    plt.clf()

def prepare_data_to_predict(ultimosDias, scaler, PASOS=PASOS):
    values = ultimosDias.values
    values = values.astype('float32')
    # normalize features
    values=values.reshape(-1, 1) # esto lo hacemos porque tenemos 1 sola dimension
    scaled = scaler.fit_transform(values)
    reframed = series_to_supervised(scaled, PASOS, 1)
    reframed.drop(reframed.columns[[7]], axis=1, inplace=True)
    reframed.head(7)

    # reshape input
    values = reframed.values
    x_test = values[6:, :]
    x_test = x_test.reshape((x_test.shape[0], 1, x_test.shape[1]))
    return x_test


def predict_next_days(model, scaler, x_test, days=7):
    def agregarNuevoValor(x_test, nuevoValor):
        for i in range(x_test.shape[2]-1):
            x_test[0][0][i] = x_test[0][0][i+1]
        x_test[0][0][x_test.shape[2]-1]=nuevoValor
        return x_test
    # Predict X values
    results=[]
    for i in range(days):
        parcial=model.predict(x_test)
        results.append(parcial[0])
        # print(x_test)
        x_test=agregarNuevoValor(x_test,parcial[0])
    adimen = [x for x in results]
    # print(adimen)
    inverted = scaler.inverse_transform(adimen)
    predicted = pd.DataFrame(inverted)
    predicted.columns = ['pronostico']
    # predicted.plot()
    return predicted

def show_predicted_image(instance, predicted):
    # Generate Probable services
    figure = io.BytesIO()
    plt.figure(figsize=(12, 8))
    plt.plot(predicted['pronostico'])
    plt.ylabel('Comentarios')
    plt.xlabel('Siguientes Dias')
    plt.title('Probables Comentarios en los siguientes dias')
    # plt.show()
    plt.savefig(figure, format='png')
    content_file = ImageFile(figure)
    # add random file name
    name_file = f'predicted-{timedelta(days=7)}.png'
    instance.image_predicted_7_days.save(name_file, content_file)
    plt.clf()


# is_presupuesto=True or publicaciones
def main_generate_predictible(model_instance, predict_days=7):
    """
    Main function to generate the predictions
    """
    cvs_generated = generate_cvs_publicaciones()

    # Read cvs and generate data frame
    df = read_cvs_and_generate_data_frame(cvs_generated)

    # number total of rows in df, if not exist gone
    if df.shape[0] == 0:
        return None

    reframed, scaler = preparate_keras_data(df)

    # Generate the values to train and test the model
    num_rows = df.shape[0]
    if num_rows == 0:
        raise Exception('No data to train the model')

    x_train, y_train, x_val, y_val = split_train_test_set(reframed, num_rows)

    # Generate the model with keras-tensoflow
    model = make_model_keras()

    model_trained = train_model(model, x_train, y_train, x_val, y_val)

    results = model_trained.predict(x_val)

    show_results_accuracy(model_instance, results, y_val, x_val)
    # # show_history_loss(model_trained) # not work
    comparate_results(model_instance, scaler, results, y_val)

    # # Used to feed the model and generate the prediction
    last_days = df.tail(30)

    # # Convert last days in matrix to feed the model
    pre_values_x = prepare_data_to_predict(last_days, scaler, PASOS)
    from pprint import pprint
    pprint(pre_values_x)

    # # Predict next days
    predicted = predict_next_days(model_trained, scaler, pre_values_x, 7) # default 7 days

    # # Generate Predicted image and save in database
    show_predicted_image(model_instance, predicted)

    # # Get the list of services predicted in float values
    list_predicted = predicted['pronostico'].tolist()

    # # convert list of float generated by tensorflow into int round values
    convert_list_predicted = set([int(round(x)) for x in list_predicted])
    return convert_list_predicted

