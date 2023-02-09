from django.urls import path
from. import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registros', views.registros, name='registros'),
    path('registros/crear', views.crear, name='crear'),
    path('registros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('registros/editar/<int:id>', views.editar, name='editar'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)