from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/clientes/', include('apps.cliente.urls')),

]
