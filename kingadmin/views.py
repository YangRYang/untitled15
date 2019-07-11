from django.shortcuts import render,HttpResponse
from kingadmin.site import site
from kingadmin.app_setup import kingadmin_auto_discover
kingadmin_auto_discover()
# Create your views here.
def psm(request):
    return render(request,'kingadmin/haha.html')

def ssk(request):
    return render(request,'king/laozi.html')

def showcustemor(request):
    return render(request,'king/base.html')

def float(request):
    return render(request,'king/float.html')

def sitea(request):
    print(dir(site))
    print(site.youwrite)
    return HttpResponse(site)