from django.shortcuts import render,HttpResponse
from kingadmin.site import site
from kingadmin.app_setup import kingadmin_auto_discover
kingadmin_auto_discover()
# Create your views here.
def psm(request):
    return render(request,'kingadmin/haha.html')

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
    app_name=[]
    for app in site.youwrite:
        app_name.append(app)


    return render(request,'kingadmin/app_index.html',{'app_name':app_name})