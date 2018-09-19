from django.urls import path

from . import views
# from django.views.generic import TemplateView
from catalog.views import UnitView

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),

    # path('units/$', UnitView.as_view(template_name="unit.html")),
    
    path('units/<int:unitpk>/', UnitView.as_view(), name='unit'),

    path('units/', views.units, name='units'),
    path('units/byabbra', views.unitsabbra, name='units'),
    path('units/byabbrz', views.unitsabbrz, name='units'),
    path('units/bynamea', views.unitsnamea, name='units'),
    path('units/bynamez', views.unitsnamez, name='units'),
    path('units/bydatenew', views.unitsdatenew, name='units'),
    path('units/bydateold', views.unitsdateold, name='units'),
    path('units/byprenamea', views.unitsprenamea, name='units'),
    path('units/byprenamez', views.unitsprenamez, name='units'),
    

    path('details/', views.details, name='details'),
    path('details/bynamea', views.detailsnamea, name='details'),
    path('details/bynamez', views.detailsnamez, name='details'),
    path('details/bymetaltypea', views.metaltypea, name='details'),
    path('details/bymetaltypez', views.metaltypez, name='details'),
    path('details/byсoatingclassa', views.сoatingclassa, name='details'),
    path('details/byсoatingclassz', views.сoatingclassz, name='details'),
    path('details/bydatenew', views.detailsdatenew, name='details'),
    path('details/bydateold', views.detailsdateold, name='details'),

    path('catalog/', views.catalog, name='catalog'),
    path('catalog/bynamea', views.catalognamea, name='catalog'),
    path('catalog/bynamez', views.catalognamez, name='catalog'),
    path('catalog/bydatenew', views.catalogdatenew, name='catalog'),
    path('catalog/bydateold', views.catalogdateold, name='catalog'),
]