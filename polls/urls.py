import imp
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views
from . import plots
from . import prediccion
from . import prediccion_lineal
urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('plots', plots.index, name='buscar'),
    path('ggplot',prediccion.ggplot, name='ggplot'),
    path('lineal',prediccion_lineal.prediccionLineal, name='lineal')
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)