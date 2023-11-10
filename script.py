from datetime import timedelta, datetime, date
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from core.predictions.ia_models.prophet_services import main_generate_predictible
from core.predictions.ia_models.prophet_landing import main_generate_predictible as forecasting_landing
from core.predictions.ia_models.tensor_servicio import main_generate_predictible as generate_tensor_servicio
from core.predictions.ia_models.tensor_publicacion import main_generate_predictible as generate_tensor_publicacion

from core.predictions.models import (
    PredictedData,
    Servicios,
    PredictedDataTensorFlowModel,
    PredictedDataForPublicacionesFacebook,
    PublicacionesFacebook,
    PredictedDataProphetResumen,
    LandingPageUsuarios,
    PredictedProphetLandingModel,
    PredictedLandingResumen,
)

# today date
TODAY = timezone.now().date().today() - timedelta(days=1)

"""
Prophet function
"""
# {'most_probable': 127, 'lest_probable_low': 65, 'lest_probable_high': 189, 'date': datetime.date(2023, 10, 24)}
def generate_prophet_servicios():
    # Clean PredictedData
    PredictedData.objects.all().delete()
    PredictedDataProphetResumen.objects.all().delete()


    instance = PredictedDataProphetResumen.objects.create()
    all_probable = main_generate_predictible(instance, TODAY)

    data = []
    services_counter = 1
    for service in all_probable:
        print(service)
        try:
            service_most = Servicios.objects.get(id_servicio=service['most_probable'])
            service_low = Servicios.objects.get(id_servicio=service['less_probable_low'])
            service_high = Servicios.objects.get(id_servicio=service['less_probable_high'])
        except Exception as e:
            print(e)
            continue
        services_counter = services_counter+ 1

        data.append(PredictedData(
                service=service_most,
                less_probable_low=service_low,
                less_probable_high=service_high,
                date_predict=service['date_predict'],
        ))
        if services_counter == 30:
            break
    PredictedData.objects.bulk_create(data)
    print(f"Prophet function finished (Generated {services_counter} predictions)...")


def generate_prophet_landing():
    # Clean PredictedData
    PredictedProphetLandingModel.objects.all().delete()
    PredictedLandingResumen.objects.all().delete()

    instance = PredictedProphetLandingModel.objects.create()
    all_probable = forecasting_landing(instance, TODAY)

    data = []
    services_counter = 1
    for landing in all_probable:
        try:
            landing_most = LandingPageUsuarios.objects.filter(TOTAL_CLICKS=landing['most_probable'])
            landing_low = LandingPageUsuarios.objects.filter(TOTAL_CLICKS=landing['less_probable_low'])
            landing_high = LandingPageUsuarios.objects.filter(TOTAL_CLICKS=landing['less_probable_high'])
        except Exception as e:
            print('(Errors) No values: ', landing)
            print(e)
            continue

        p = PredictedLandingResumen.objects.create(
                date_predict=landing['date_predict'],
        )
        p.landing_most.set(landing_most)
        p.landing_less_low.set(landing_low)
        p.landing_less_high.set(landing_high)
        services_counter = services_counter+ 1

    print(f"Prophet Landing Page function finished (Generated {services_counter} predictions)...")


""" 
Keras-Tensorflow model for predict 7 productos more probables tomorrow
"""
def run_tensorflow_predictions_services():
    # clean PredictedDataTensorFlowModel
    PredictedDataTensorFlowModel.objects.all().delete()

    # create instance
    model_instance = PredictedDataTensorFlowModel.objects.create()

    # generate tensorflow info
    convert_list_predicted = generate_tensor_servicio(model_instance)
    services = Servicios.objects.filter(id_servicio__in=convert_list_predicted)
    model_instance.services.set(services)
    print("Predictions probable services IDs: ", convert_list_predicted)
    print("Keras-Tensorflow Services function finished...")


""" 
Keras-Tensorflow model for predict 7 productos more probables tomorrow
"""
def run_tensorflow_predictions_publicaciones(is_presupuesto=False):
    # clean PredictedDataTensorFlowModel
    # PredictedDataTensorFlowModel.objects.all().delete()
    # clean
    PredictedDataForPublicacionesFacebook.objects.all().delete()

    # create instance
    model_instance = PredictedDataForPublicacionesFacebook.objects.create()

    # generate tensorflow info
    convert_list_predicted = generate_tensor_publicacion(model_instance, is_presupuesto)

    if not convert_list_predicted:
        print('NO HAY DATOS PARA PREDECIR LAS PUBLICACIONES DE FACEBOOK (Check there is no comentarios)')
        return

    pubs = PublicacionesFacebook.objects.filter(comentarios__in=list(convert_list_predicted))
    if pubs:
        model_instance.publications.set(pubs)

    print("Keras-Tensorflow Publications Facebook function finished...")


# Runing from shell
if __name__ == "django.core.management.commands.shell":
    # call prophet function
    generate_prophet_servicios()

    generate_prophet_landing()

    # call keras-tensorflow function
    run_tensorflow_predictions_services()

    # # Tensorflow predictions for Publications
    run_tensorflow_predictions_publicaciones()


