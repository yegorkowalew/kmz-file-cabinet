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

    path('details', views.details, name='details'),
    path('details/bynamea', views.detailsnamea, name='details'),
    path('details/bynamez', views.detailsnamez, name='details'),
    path('details/bydatenew', views.detailsdatenew, name='details'),
    path('details/bydateold', views.detailsdateold, name='details'),
]