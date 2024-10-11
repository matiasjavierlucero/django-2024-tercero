from rest_framework.routers import DefaultRouter, path

from api_v1.views.products import (
    ProductModelViewSet, 
    ProductApiView, 
    ProductListCreateGenericAPIView,
    ProductReadOnly,
)
from api_v1.views.emails import send_test_email


# UTILIZADO PARA MODELVIEWSET
router = DefaultRouter()
router.register(r'products', ProductModelViewSet, 'products')
router.register(r'products_readonly', ProductReadOnly, 'products_readonly')

# PARA EL USO DE APIVIEWS
urlpatterns = [
    path(
        'products_apiview', ProductApiView.as_view(), name='product_apiview'
    ),
    path(
        'products_apiview/<int:pk>', 
        ProductApiView.as_view(), 
        name='product_apiview_detail'
    ),
    path(
        'products_generic_apiview', 
        ProductListCreateGenericAPIView.as_view(),
        name='products_generic_apiview'
    ),
    path(
        'products_generic_apiview/<int:pk>', 
        ProductListCreateGenericAPIView.as_view(),
        name='products_generic_apiview_retrieve'
    ),
    path('send_email/', send_test_email, name='send_email')
]

urlpatterns += router.urls
