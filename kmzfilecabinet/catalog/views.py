from django.shortcuts import render
from django.db.models import F, Value
from django.db.models.functions import Concat

from django.http import HttpResponse
from django.template.response import TemplateResponse

from .models import Unit, Detail, UnitContentPhoto
from django.contrib.admin.models import LogEntry
import logging

from itertools import chain
from operator import attrgetter

from django.views.generic.base import TemplateView

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


logger = logging.getLogger('catalog')

per_page = 23

def index(request):
    """
    Главная страница. Выборки: количество узлов, деталей. Лог админки.
    """
    admin_log = LogEntry.objects.order_by('-action_time')[:25]
    title = "Главная"
    len_unit = Unit.objects.count()
    len_detail = Detail.objects.count()
    all_count = len_unit + len_detail

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'index.html', {'output': Unit.objects.order_by('-edit_date'), 
                                                    'title':title, 
                                                    'len_unit':len_unit,
                                                    'len_detail':len_detail,
                                                    'admin_log':admin_log,
                                                    'units_count':len_unit,
                                                    'details_count':len_detail,
                                                    'all_count':all_count,
                                                    })

"""
Выборки каталога
"""

@login_required(login_url='/accounts/login/')
def catalog(request):
    """
    Страница каталога. Объединяю в одну выборку модели Details и Units
    """
    title = "Каталог"
    unit_all = Unit.objects.annotate(url=Concat(Value('/units/'), F('pk')))
    len_unit = unit_all.count()
    detail_all = Detail.objects.annotate(name=F('nom_num'), url=Concat(Value('/details/'), F('pk')))
    len_detail = detail_all.count()
    result_list = list(chain(unit_all, detail_all))

    paginator = Paginator(result_list, per_page)
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'catalog.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def catalognamea(request):
    """
    Страница каталога. Объединяю в одну выборку модели Details и Units. Сортирую по имени
    """
    title = "Каталог. По имени: А-Я"
    unit_all = Unit.objects.annotate(url=Concat(Value('/units/'), F('pk')))
    len_unit = unit_all.count()
    detail_all = Detail.objects.annotate(name=F('nom_num'), url=Concat(Value('/details/'), F('pk')))
    len_detail = detail_all.count()
    result_list = sorted(
        chain(unit_all, detail_all),
        key=attrgetter('name'))

    paginator = Paginator(result_list, per_page)
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'catalognamea.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def catalognamez(request):
    """
    Страница каталога. Объединяю в одну выборку модели Details и Units. Сортирую по имени в обратном порядке
    """
    title = "Каталог. По имени: Я-А"
    unit_all = Unit.objects.annotate(url=Concat(Value('/units/'), F('pk')))
    len_unit = unit_all.count()
    detail_all = Detail.objects.annotate(name=F('nom_num'), url=Concat(Value('/details/'), F('pk')))
    len_detail = detail_all.count()
    result_list = sorted(
        chain(unit_all, detail_all),
        key=attrgetter('name'), reverse=True)

    paginator = Paginator(result_list, per_page)
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'catalognamez.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def catalogdatenew(request):
    """
    Страница каталога. Объединяю в одну выборку модели Details и Units. Сортирую по дате
    """
    title = "Каталог. По дате: сначала новые"
    unit_all = Unit.objects.annotate(url=Concat(Value('/units/'), F('pk')))
    len_unit = unit_all.count()
    detail_all = Detail.objects.annotate(name=F('nom_num'), url=Concat(Value('/details/'), F('pk')))
    len_detail = detail_all.count()
    result_list = sorted(
        chain(unit_all, detail_all),
        key=attrgetter('edit_date'))

    paginator = Paginator(result_list, per_page)
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'catalogdatenew.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def catalogdateold(request):
    """
    Страница каталога. Объединяю в одну выборку модели Details и Units. Сортирую по дате в обратном порядке
    """
    title = "Каталог. По дате: сначала старые"
    unit_all = Unit.objects.annotate(url=Concat(Value('/units/'), F('pk')))
    len_unit = unit_all.count()
    detail_all = Detail.objects.annotate(name=F('nom_num'), url=Concat(Value('/details/'), F('pk')))
    len_detail = detail_all.count()
    result_list = sorted(
        chain(unit_all, detail_all),
        key=attrgetter('edit_date'), reverse=True)

    paginator = Paginator(result_list, per_page)
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'catalogdateold.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

"""
Выборки по узлам
"""

@login_required(login_url='/accounts/login/')
def units(request):
    """
    Главная страница. Выборки: количество узлов, деталей. Лог админки.
    """
    title = "Узлы"
    result_list = Unit.objects.all()
    len_unit = result_list.count()
    len_detail = Detail.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'units.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def unitsabbra(request):
    """
    Узлы. По аббревиатуре: А-Я
    """
    title = "Узлы. По имени: А-Я"
    result_list = Unit.objects.order_by('abbrname')
    len_unit = result_list.count()
    len_detail = Detail.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'unitsabbra.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def unitsabbrz(request):
    """
    Узлы. По аббревиатуре: Я-А
    """
    title = "Узлы. По имени: Я-А"
    result_list = Unit.objects.order_by('-abbrname')
    len_unit = result_list.count()
    len_detail = Detail.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'unitsabbrz.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def unitsnamea(request):
    """
    Узлы. По имени: А-Я
    """
    title = "Узлы. По имени: А-Я"
    result_list = Unit.objects.order_by('name')
    len_unit = result_list.count()
    len_detail = Detail.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'unitsnamea.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def unitsnamez(request):
    """
    Узлы. По имени: Я-А
    """
    title = "Узлы. По имени: Я-А"
    result_list = Unit.objects.order_by('-name')
    len_unit = result_list.count()
    len_detail = Detail.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'unitsnamez.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def unitsdatenew(request):
    """
    Узлы. По дате: сначала новые. Выборки: узлы по дате
    """
    title = "Узлы. Сортировка по дате: сначала новые."
    result_list = Unit.objects.order_by('edit_date')
    len_unit = result_list.count()
    len_detail = Detail.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'unitsdatenew.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def unitsdateold(request):
    """
    Узлы. По дате: сначала старые. Выборки: узлы по дате
    """
    title = "Узлы. Сортировка по дате: сначала старые."
    result_list = Unit.objects.order_by('-edit_date')
    len_unit = result_list.count()
    len_detail = Detail.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'unitsdateold.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def unitsprenamea(request):
    """
    Узлы. По типу: А-Я
    """
    title = "Узлы. По типу: А-Я"
    result_list = Unit.objects.order_by('prename')
    len_unit = result_list.count()
    len_detail = Detail.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'unitsprenamea.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def unitsprenamez(request):
    """
    Узлы. По типу: Я-А
    """
    title = "Узлы. По типу: Я-А"
    result_list = Unit.objects.order_by('-prename')
    len_unit = result_list.count()
    len_detail = Detail.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'unitsprenamez.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

"""
Выборки по деталям
"""

@login_required(login_url='/accounts/login/')
def details(request):
    """
    Главная страница. Выборки: количество узлов, деталей. Лог админки.
    """
    title = "Детали"

    result_list = Detail.objects.all()
    len_detail = result_list.count()
    len_unit = Unit.objects.count()
    paginator = Paginator(result_list, per_page) 

    page = request.GET.get('page')
    result_list = paginator.get_page(page)
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'details.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def detailsnamea(request):
    """
    Детали. По имени: А-Я
    """
    title = "Детали. По имени: А-Я"
    result_list = Detail.objects.order_by('nom_num')
    len_detail = result_list.count()
    len_unit = Unit.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsnamea.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def detailsnamez(request):
    """
    Детали. По имени: Я-А
    """
    title = "Детали. По имени: Я-А"
    result_list = Detail.objects.order_by('-nom_num')
    len_detail = result_list.count()
    len_unit = Unit.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsnamez.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def metaltypea(request):
    """
    Детали. По типу металла: А-Я
    """
    title = "Детали. По типу металла: А-Я"
    result_list = Detail.objects.order_by('metaltype')
    len_detail = result_list.count()
    len_unit = Unit.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsmetaltypea.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def metaltypez(request):
    """
    Детали. По типу металла: Я-А
    """
    title = "Детали. По типу металла: Я-А"
    result_list = Detail.objects.order_by('-metaltype')
    len_detail = result_list.count()
    len_unit = Unit.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsmetaltypez.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def сoatingclassa(request):
    """
    Детали. По типу металла: А-Я
    """
    title = "Детали. По типу металла: А-Я"
    result_list = Detail.objects.order_by('сoatingclass')
    len_detail = result_list.count()
    len_unit = Unit.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsсoatingclassa.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def сoatingclassz(request):
    """
    Детали. По типу металла: Я-А
    """
    title = "Детали. По типу металла: Я-А"

    result_list = Detail.objects.order_by('-сoatingclass')
    len_detail = result_list.count()
    len_unit = Unit.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsсoatingclassz.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

@login_required(login_url='/accounts/login/')
def detailsdatenew(request):
    """
    Детали. По дате: сначала новые. Выборки: узлы по дате
    """
    title = "Детали. Сортировка по дате: сначала новые."
    result_list = Detail.objects.order_by('edit_date')
    len_detail = result_list.count()
    len_unit = Unit.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsdatenew.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })
    
@login_required(login_url='/accounts/login/')
def detailsdateold(request):
    """
    Детали. По дате: сначала старые. Выборки: узлы по дате
    """
    title = "Детали. Сортировка по дате: сначала старые."
    result_list = Detail.objects.order_by('-edit_date')
    len_detail = result_list.count()
    len_unit = Unit.objects.count()

    paginator = Paginator(result_list, per_page) 
    page = request.GET.get('page')
    result_list = paginator.get_page(page)

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return render(request, 'detailsdateold.html', {'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

class UnitView(TemplateView):
    template_name = "unit.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unit'] = Unit.objects.get(pk=context['unitpk'])
        context['title'] = context['unit'].name
        context['images'] = UnitContentPhoto.objects.filter(unit__pk=context['unitpk'])
        # print(context['images'])
        logger.info('"%s" page visited. User: %s' % (context['title'], self.request.user))
        return context

class DetailView(TemplateView):
    template_name = "detail.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = Detail.objects.get(pk=context['detailpk'])
        context['title'] = context['detail'].nom_num
        # context['images'] = UnitContentPhoto.objects.filter(unit__pk=context['unitpk'])
        # print(context['images'])
        logger.info('"%s" page visited. User: %s' % (context['title'], self.request.user))
        return context

