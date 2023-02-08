from django.urls import path
from. import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('consulta', views.consulta, name='consulta'),
]