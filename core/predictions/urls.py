from django.urls import path
from core.predictions.views import (
    ChartByQuantityView,
    ChartByValueView,
    PredictionView,
    PredictionViewThirty,
    PredictionPublicationFacebookView,
    PredictionLandingPageView,
)

app_name = "predictions"

urlpatterns = [
    path("by-quantity/", ChartByQuantityView.as_view(), name="prediction_quantity"),
    path("by-value/", ChartByValueView.as_view(), name="prediction_value"),

    # predictions
    path("future/", PredictionView.as_view(), name="predictions_view"),
    path("future/30/", PredictionViewThirty.as_view(), name="predictions_view_thirty"),
    path("publications/facebook/", PredictionPublicationFacebookView.as_view(), name="prediction_publication_facebook"),
    path("landing/", PredictionLandingPageView.as_view(), name="predictions_landing"),
]
