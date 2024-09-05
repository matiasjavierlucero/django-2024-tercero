from rest_framework.routers import DefaultRouter

from api_v1.views.products import ProducViewSet

router = DefaultRouter()
router.register(r'products', ProducViewSet, 'products')

urlpatterns = router.urls