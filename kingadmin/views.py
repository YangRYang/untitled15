from django.shortcuts import render, HttpResponse
from kingadmin.site import site
from kingadmin.app_setup import kingadmin_auto_discover

kingadmin_auto_discover()


# Create your views here.
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
    return render(request,'kingadmin/model.html',{'site':site.youwrite})

def  table_obj_list_add(request, app, model):
    return render(request,'kingadmin/add.html')