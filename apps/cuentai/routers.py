from rest_framework.routers import DefaultRouter
from .views import CuentAIFlowViewSet

router = DefaultRouter()

router.register(r'',CuentAIFlowViewSet, basename='cuentai')

urlpatterns = router.urls