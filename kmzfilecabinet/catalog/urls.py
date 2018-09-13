from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('units', views.units, name='units'),
    path('units/bynamea', views.unitsnamea, name='units'),
    path('units/bynamez', views.unitsnamez, name='units'),
    path('units/bydatenew', views.unitsdatenew, name='units'),
    path('units/bydateold', views.unitsdateold, name='units'),
    path('units/byprenamea', views.unitsprenamea, name='units'),
    path('units/byprenamez', views.unitsprenamez, name='units'),


]