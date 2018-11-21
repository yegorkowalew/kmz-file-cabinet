from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models import Unit, Detail

from django.core.serializers import serialize

@login_required(login_url='/accounts/login/')
def search(request):
    """
    Поиск
    """
    title = "Поиск"
    result_list = Detail.objects.all()
    len_detail = result_list.count()
    len_unit = Unit.objects.count()
    return render(request, 'search.html', {
# 'result_list':result_list, 
                                            'title':title,
                                            'units_count':len_unit,
                                            'details_count':len_detail,
                                            'all_count':len_unit+len_detail,
                                            })

import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
@login_required(login_url='/accounts/login/')
def searchajax(request, name):
    # print(name + ' <')
    # data = Detail.objects.filter(designation__icontains='СМВУ').values('designation', 'nom_num')
    # ser_data =  serializers.serialize('json', data)
    data =  serializers.serialize('json', Detail.objects.filter(designation__icontains=name))
    # print(data)
    return HttpResponse(data, content_type='application/json')