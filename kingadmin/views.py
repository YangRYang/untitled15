from django.shortcuts import render, HttpResponse
from kingadmin.site import site
from kingadmin.app_setup import kingadmin_auto_discover
from django.forms import forms, ModelForm
from kingadmin import models

kingadmin_auto_discover()

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
    data = model_class.model.objects.all()
    return render(request, 'kingadmin/model.html', {'site': site.youwrite,'queryset':data,'model_class':model_class})


def table_obj_list_add(request, app, model):
    return render(request, 'kingadmin/add.html')

def table_obj_list_change(request, app, model):
    return render(request, 'kingadmin/add.html')
