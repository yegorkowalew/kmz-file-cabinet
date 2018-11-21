from django.urls import path

from . import views
# from django.views.generic import TemplateView
from catalog.views import UnitView, DetailView

from django.conf import settings
from django.conf.urls.static import static

app_name = 'search'

urlpatterns = [
    path('', views.search, name='search'),
    path('<name>', views.searchajax, name='searchajax')
]
