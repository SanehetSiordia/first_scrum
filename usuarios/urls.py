from django.urls import path
from. import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registros', views.registros, name='registros'),
    path('registros/crear', views.crear, name='crear'),
    path('registros/editar', views.editar, name='editar'),
]