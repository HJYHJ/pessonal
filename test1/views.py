from django.http import  HttpResponse
from django.shortcuts import render,redirect
from test1.models import *
from .forms import otBoysInfoForm
# Create your views here.
def index(request):
    yukino = girl.objects.all()

    for i in yukino:
        i.habbits=i.habbits.split(",")
    print(yukino)
    return render(request,'index.html',{'li':yukino} )

def lvpeisong(request):
    client_ip=request.META.get('REMOTE_ADDR')
    print(client_ip)
    return render(request,'lvpeisong.html',{'client_ip':client_ip})
def chenyiming(request):
    client_ip = request.META.get('REMOTE_ADDR')
    print(client_ip)
    return render(request,'chenyiming.html',{'client_ip':client_ip})
def liuhangdong(request):
    client_ip = request.META.get('REMOTE_ADDR')
    print(client_ip)
    return render(request,'liuhangdong.html',{'client_ip':client_ip})
def jiayawei(request):
    client_ip = request.META.get('REMOTE_ADDR')
    print(client_ip)
    return render(request,'jiayawei.html',{'client_ip':client_ip})
def leiyaxi(request):
    client_ip = request.META.get('REMOTE_ADDR')
    print(client_ip)
    return render(request,'leiyaxi.html',{'client_ip':client_ip})

def create_otboys(request):
    if request.method=='POST':
        form = otBoysInfoForm(request.POST,request.FILES)
        if form.is_valid():
            info = form.save(commit=False)
            info.save()
            form.save_m2m()
            return redirect('index.html')
    else:
        form = otBoysInfoForm()
    return render(request,'Insert.html',{'form':form})
def tocreate(request):
    print(1)
    return 'Insert.html'