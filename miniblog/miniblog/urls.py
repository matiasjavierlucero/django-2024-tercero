from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api_v1/', include('api_v1.urls')),
 ] + static (
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
