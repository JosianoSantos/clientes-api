from django.urls import path

from . import views

app_name='cliente'
urlpatterns = [
    path('', views.ClienteList.as_view(), name='list'),
    path('create', views.ClienteCreate.as_view(), name='create'),
    path('update/<int:id>', views.ClienteUpdate.as_view(), name='update'),
    path('detail/<int:id>', views.ClienteDetail.as_view(), name='detail'),
    path('delete/<int:id>', views.ClienteDelete.as_view(), name='delete'),

]