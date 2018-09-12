from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.response import TemplateResponse

from .models import Unit, Detail
from django.contrib.admin.models import LogEntry

def index(request):
    admin_log = LogEntry.objects.order_by('-action_time')[:25]
    title = "Главная"
    len_unit = Unit.objects.count() #len(Unit.objects.all())
    len_detail = Detail.objects.count() #len(Detail.objects.all())
    return TemplateResponse(request, 'index.html', {'output': Unit.objects.order_by('-edit_date'), 
                                                    'title':title, 
                                                    'len_unit':len_unit,
                                                    'len_detail':len_detail,
                                                    'admin_log':admin_log,
                                                    })

def units(request):
    title = "Узлы"
    return TemplateResponse(request, 'units.html', {'output': Unit.objects.order_by('-edit_date'), 'title':title})