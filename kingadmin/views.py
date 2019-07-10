from django.shortcuts import render

# Create your views here.
def psm(request):
    return render(request,'kingadmin/haha.html')

def ssk(request):
    return render(request,'king/laozi.html')

def showcustemor(request):
    return render(request,'king/base.html')

def float(request):
    return render(request,'king/float.html')