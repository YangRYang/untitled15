from django.shortcuts import render, HttpResponse
from kingadmin.site import site
from kingadmin.app_setup import kingadmin_auto_discover
from django.forms import forms, ModelForm
from kingadmin import models

kingadmin_auto_discover()
def get_search_result(data , request,model_class):
    # print(request.GET)
    search_key = request.GET.get('_q','')
    model_class.search_value = search_key
    if  search_key:
        print('yyy')

        data = data.filter(name__contains=search_key)
    # data = data.filter(search_key)
    return data


def psm(request):
    return render(request, 'kingadmin/haha.html')


def ssk(request):
    return render(request, 'kingadmin/laozi.html')


def showcustemor(request):
    return render(request, 'kingadmin/base.html')


def float(request):
    return render(request, 'kingadmin/float.html')


def sitea(request):
    print(dir(site))
    print(site.youwrite)
    return HttpResponse(site)


def app_index(request):
    return render(request, 'kingadmin/app_index.html', {'site': site.youwrite})


def table_obj_list(request, app, model):
    model_class = site.youwrite[app][model]

    if request.method =='POST':
        pass
    data = model_class.model.objects.all()
    data = get_search_result(data,request,model_class)
    return render(request, 'kingadmin/model.html', {'site': site.youwrite,'queryset':data,'model_class':model_class})


def table_obj_list_add(request, app, model):
    return render(request, 'kingadmin/add.html')

def table_obj_list_change(request, app, model):
    return render(request, 'kingadmin/add.html')
