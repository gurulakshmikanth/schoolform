from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse


def create_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        QLTO=Topic.objects.all()
        d={'topic':QLTO}
        return render(request,'display_topic.html',d)


    return render(request,'create_topic.html')

def create_webpage(request):
    QLWO=Topic.objects.all()
    d={'web':QLWO}
    if request.method=='POST':
        wn=request.POST['tn']
        n=request.POST['na']
        u=request.POST['ur']
        e=request.POST['em']
        wnn=Topic.objects.get(topic_name=wn)
        wo=Webpage.objects.get_or_create(topic_name=wnn,name=n,url=u,email=e)[0]
        wo.save()
        Webpage.objects.filter(topic_name='kabaddi').update(url='https://rahul.in',email='rahul@gmail.com')
        QW=Webpage.objects.all()
        d1={'web1':QW}
        return render(request,'display_webpage.html',d1)
    return render(request,'create_webpage.html',d)

def create_access(request):
    QLAO=Webpage.objects.all()
    d={'acces':QLAO}
    if request.method=='POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']

        ao=Webpage.objects.get(pk=na)
        aoo=AccessRecords.objects.get_or_create(name=ao,author=au,date=da)[0]
        aoo.save()
        ac=AccessRecords.objects.all()
        d1={'access1':ac}
        return render(request,'display_access.html',d1)

    return render(request,'create_access.html',d)


def select_multiple_webpage(request):
    QLTO=Webpage.objects.all()
    d={'web':QLTO}
    if request.method=='POST':
        tn=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in tn:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        d1={'web1':QLWO}
        return render(request,'display_multiple.html',d1)
    return render(request,'select_multiple_webpage.html',d)


def select_multiple_access(request):
    QLAO=AccessRecords.objects.all()
    d={'acc':QLAO}
    return render(request,'select_multiple_access.html',d)


def checkbox_topic(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    if request.method=='POST':
        tn=request.POST.getlist('tn')
        QLTO=Topic.objects.none()
        for i in tn:
            QLTO=QLTO|Topic.objects.filter(topic_name=i)
        d1={'topic1':QLTO}
        return render(request,'checkbox_display_topic.html',d1)


    return render(request,'checkbox_topic.html',d)