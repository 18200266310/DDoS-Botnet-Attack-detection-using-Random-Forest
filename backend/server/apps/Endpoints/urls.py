# backend/server/apps/endpoints/urls.py file
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.Endpoints.views import EndpointViewSet
from apps.Endpoints.views import MLAlgorithmViewSet
from apps.Endpoints.views import MLAlgorithmStatusViewSet
from apps.Endpoints.views import MLRequestViewSet
from apps.Endpoints.views import PredictView
from apps.Endpoints.views import ABTestViewSet
from apps.Endpoints.views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register(r"Endpoints", EndpointViewSet, basename="Endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),

    url(
        r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),
    url(
        r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)", StopABTestView.as_view(), name="stop_ab"
    ),
]
