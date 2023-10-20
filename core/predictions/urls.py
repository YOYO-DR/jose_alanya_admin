from django.urls import path
from core.predictions.views import ChartByQuantityView, ChartByValueView

app_name = "predictions"

urlpatterns = [
    path("by-quantity/", ChartByQuantityView.as_view(), name="prediction_quantity"),
    path("by-value/", ChartByValueView.as_view(), name="prediction_value"),
]
