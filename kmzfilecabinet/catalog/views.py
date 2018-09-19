from django.shortcuts import render
from django.db.models import F, Value
from django.db.models.functions import Concat

# Create your views here.
from django.http import HttpResponse
from django.template.response import TemplateResponse

from .models import Unit, Detail
from django.contrib.admin.models import LogEntry
import logging

from django.core.paginator import Paginator

logger = logging.getLogger('catalog')

per_page = 5

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

def catalog(request):
    """
    Страница каталога. Объединяю в одну выборку модели Details и Units
    """
    admin_log = LogEntry.objects.order_by('-action_time')[:25]
    title = "Каталог"

    from itertools import chain 
    unit_all = Unit.objects.annotate(url=Concat(Value('/units/'), F('pk')))
    unit_all.values("name", "url")
    detail_all = Detail.objects.annotate(name=F('nom_num'), url=Concat(Value('/details/'), F('pk')))
    unit_all.values("name", "url")
    result_list = list(chain(unit_all, detail_all))

    paginator = Paginator(result_list, per_page) # Show 25 contacts per page

    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'catalog.html', {'result_list':result_list,})


"""
Выборки по узлам
"""

def units(request):
    """
    Главная страница. Выборки: количество узлов, деталей. Лог админки.
    """
    title = "Узлы"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    result_list = Unit.objects.order_by('-edit_date')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    return render(request, 'units.html', {'result_list':result_list, 'title':title})

def unitsabbra(request):
    """
    Узлы. По аббревиатуре: А-Я
    """
    title = "Узлы. По имени: А-Я"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    result_list = Unit.objects.order_by('abbrname')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    return render(request, 'unitsabbra.html', {'result_list':result_list, 'title':title})

def unitsabbrz(request):
    """
    Узлы. По аббревиатуре: Я-А
    """
    title = "Узлы. По имени: Я-А"
    logger.info('"%s" page visited. User: %s' % (title, request.user))

    result_list = Unit.objects.order_by('-abbrname')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    return render(request, 'unitsabbrz.html', {'result_list':result_list, 'title':title})

def unitsnamea(request):
    """
    Узлы. По имени: А-Я
    """
    title = "Узлы. По имени: А-Я"
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    result_list = Unit.objects.order_by('name')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    return render(request, 'unitsnamea.html', {'result_list':result_list, 'title':title})

def unitsnamez(request):
    """
    Узлы. По имени: Я-А
    """
    title = "Узлы. По имени: Я-А"
    logger.info('"%s" page visited. User: %s' % (title, request.user))

    result_list = Unit.objects.order_by('-name')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    return render(request, 'unitsnamez.html', {'result_list':result_list, 'title':title})

def unitsdatenew(request):
    """
    Узлы. По дате: сначала новые. Выборки: узлы по дате
    """
    title = "Узлы. Сортировка по дате: сначала новые."
    logger.info('"%s" page visited. User: %s' % (title, request.user))

    result_list = Unit.objects.order_by('edit_date')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    return render(request, 'unitsdatenew.html', {'result_list':result_list, 'title':title})

def unitsdateold(request):
    """
    Узлы. По дате: сначала старые. Выборки: узлы по дате
    """
    title = "Узлы. Сортировка по дате: сначала старые."
    logger.info('"%s" page visited. User: %s' % (title, request.user))

    result_list = Unit.objects.order_by('-edit_date')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    return render(request, 'unitsdateold.html', {'result_list':result_list, 'title':title})

def unitsprenamea(request):
    """
    Узлы. По типу: А-Я
    """
    title = "Узлы. По типу: А-Я"
    logger.info('"%s" page visited. User: %s' % (title, request.user))

    result_list = Unit.objects.order_by('prename')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    return render(request, 'unitsprenamea.html', {'result_list':result_list, 'title':title})

def unitsprenamez(request):
    """
    Узлы. По типу: Я-А
    """
    title = "Узлы. По типу: Я-А"
    logger.info('"%s" page visited. User: %s' % (title, request.user))

    result_list = Unit.objects.order_by('-prename')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    return render(request, 'unitsprenamez.html', {'result_list':result_list, 'title':title})

"""
Выборки по деталям
"""

def details(request):
    """
    Главная страница. Выборки: количество узлов, деталей. Лог админки.
    """
    title = "Детали"

    result_list = Detail.objects.all()
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'details.html', {'result_list':result_list, 'title':title})

def detailsnamea(request):
    """
    Детали. По имени: А-Я
    """
    title = "Детали. По имени: А-Я"

    result_list = Detail.objects.order_by('nom_num')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsnamea.html', {'result_list':result_list, 'title':title})

def detailsnamez(request):
    """
    Детали. По имени: Я-А
    """
    title = "Детали. По имени: Я-А"

    result_list = Detail.objects.order_by('-nom_num')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsnamez.html', {'result_list':result_list, 'title':title})

def metaltypea(request):
    """
    Детали. По типу металла: А-Я
    """
    title = "Детали. По типу металла: А-Я"

    result_list = Detail.objects.order_by('metaltype')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsmetaltypea.html', {'result_list':result_list, 'title':title})

def metaltypez(request):
    """
    Детали. По типу металла: Я-А
    """
    title = "Детали. По типу металла: Я-А"

    result_list = Detail.objects.order_by('-metaltype')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsmetaltypez.html', {'result_list':result_list, 'title':title})

def сoatingclassa(request):
    """
    Детали. По типу металла: А-Я
    """
    title = "Детали. По типу металла: А-Я"

    result_list = Detail.objects.order_by('сoatingclass')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsсoatingclassa.html', {'result_list':result_list, 'title':title})

def сoatingclassz(request):
    """
    Детали. По типу металла: Я-А
    """
    title = "Детали. По типу металла: Я-А"

    result_list = Detail.objects.order_by('-сoatingclass')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsсoatingclassz.html', {'result_list':result_list, 'title':title})

def detailsdatenew(request):
    """
    Детали. По дате: сначала новые. Выборки: узлы по дате
    """
    title = "Детали. Сортировка по дате: сначала новые."

    result_list = Detail.objects.order_by('edit_date')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsdatenew.html', {'result_list':result_list, 'title':title})
    
def detailsdateold(request):
    """
    Детали. По дате: сначала старые. Выборки: узлы по дате
    """
    title = "Детали. Сортировка по дате: сначала старые."

    result_list = Detail.objects.order_by('-edit_date')
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsdateold.html', {'result_list':result_list, 'title':title})
