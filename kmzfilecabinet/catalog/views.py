from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.response import TemplateResponse

from .models import Unit, Detail
from django.contrib.admin.models import LogEntry
import logging
logger = logging.getLogger('catalog')

def index(request):
    """
    Главная страница. Выборки: количество узлов, деталей. Лог админки.
    """
    admin_log = LogEntry.objects.order_by('-action_time')[:25]
    title = "Главная"
    len_unit = Unit.objects.count()
    len_detail = Detail.objects.count()
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'index.html', {'output': Unit.objects.order_by('-edit_date'), 
                                                    'title':title, 
                                                    'len_unit':len_unit,
                                                    'len_detail':len_detail,
                                                    'admin_log':admin_log,
                                                    })
"""
Выборки по узлам
"""

def units(request):
    """
    Главная страница. Выборки: количество узлов, деталей. Лог админки.
    """
    title = "Узлы"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'units.html', {'output': Unit.objects.order_by('-edit_date'), 'title':title})

def unitsnamea(request):
    """
    Узлы. По имени: А-Я
    """
    title = "Узлы. По имени: А-Я"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    req = Unit.objects.order_by('name')
    return TemplateResponse(request, 'unitsnamea.html', {'output': req, 'title':title})

def unitsnamez(request):
    """
    Узлы. По имени: Я-А
    """
    title = "Узлы. По имени: Я-А"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    req = Unit.objects.order_by('-name')
    return TemplateResponse(request, 'unitsnamez.html', {'output': req, 'title':title})

def unitsdatenew(request):
    """
    Узлы. По дате: сначала новые. Выборки: узлы по дате
    """
    title = "Узлы. Сортировка по дате: сначала новые."
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'unitsdatenew.html', {'output': Unit.objects.order_by('edit_date'), 'title':title})

def unitsdateold(request):
    """
    Узлы. По дате: сначала старые. Выборки: узлы по дате
    """
    title = "Узлы. Сортировка по дате: сначала старые."
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'unitsdateold.html', {'output': Unit.objects.order_by('-edit_date'), 'title':title})

def unitsprenamea(request):
    """
    Узлы. По типу: А-Я
    """
    title = "Узлы. По типу: А-Я"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    req = Unit.objects.order_by('prename')
    return TemplateResponse(request, 'unitsprenamea.html', {'output': req, 'title':title})

def unitsprenamez(request):
    """
    Узлы. По типу: Я-А
    """
    title = "Узлы. По типу: Я-А"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    req = Unit.objects.order_by('-prename')
    return TemplateResponse(request, 'unitsprenamez.html', {'output': req, 'title':title})

"""
Выборки по деталям
"""

def details(request):
    """
    Главная страница. Выборки: количество узлов, деталей. Лог админки.
    """
    title = "Детали"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'details.html', {'output': Detail.objects.order_by('-edit_date'), 'title':title})

def detailsnamea(request):
    """
    Детали. По имени: А-Я
    """
    title = "Детали. По имени: А-Я"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    req = Detail.objects.order_by('nom_num')
    return TemplateResponse(request, 'detailsnamea.html', {'output': req, 'title':title})

def detailsnamez(request):
    """
    Детали. По имени: Я-А
    """
    title = "Детали. По имени: Я-А"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    req = Detail.objects.order_by('-nom_num')
    return TemplateResponse(request, 'detailsnamez.html', {'output': req, 'title':title})

def detailsdatenew(request):
    """
    Детали. По дате: сначала новые. Выборки: узлы по дате
    """
    title = "Детали. Сортировка по дате: сначала новые."
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'detailsdatenew.html', {'output': Detail.objects.order_by('edit_date'), 'title':title})

def detailsdateold(request):
    """
    Детали. По дате: сначала старые. Выборки: узлы по дате
    """
    title = "Детали. Сортировка по дате: сначала старые."
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'detailsdateold.html', {'output': Detail.objects.order_by('-edit_date'), 'title':title})
