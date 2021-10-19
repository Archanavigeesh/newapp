from django.shortcuts import render
from . models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')
def new(request):
    if(request.method=='POST'):
        name=request.POST['name']
        contact=request.POST['contact']
        place=request.POST['place']
        result=request.FILES.get('result')
        checkuser=Employee.objects.filter(name=name).exists()
        msg="Username is not available"
        if checkuser:
            return render(request,'new.html',{"msg":msg})
            print(checkuser)
        else:
           registerdata=Employee(name=name,contact=contact,place=place)
           registerdata.save()
           return render(request,'new.html')
    else:
        return render(request,'new.html')


def display(request):
    if request.method=='POST':
        empobj=Employee.objects.all()
        return render(request,'display.html',{'employee':empobj})
    else:
        return render(request,'display.html')






def fnnew1(request):
    '''article_title="Python"
    article_desc="Python is a programming language"
    return render(request,'new1.html',{"article_title":article_title,"article_desc":article_desc})'''
    try:
        name=Employee.objects.all()
        print(name)
        return render(request,'new1.html',{"name":name})
    except Exception as error :
        return render(request,'new1.html',{"error":error})
def grid(request):
    return render(request,'grid.html')
def fnhome(request):
    return render(request,'home.html')
def fnabout(request):
    return render(request,'about.html')
def fndemo(x):
    if (x.method=='POST'):
        name=x.POST['name']
        contact=x.POST['contact']
        place=x.POST['place']
        demoobj=Employee(name=name,place=place,contact=contact)
        demoobj.save()
        return render(x,'demo.html')
    else:
        return render(x,'demo.html') 
    
def fnnewlogin(request):
    if(request.method=='POST'):
        try:
            name=request.POST.get('name')
            contact=request.POST.get('contact')
            place=request.POST.get('place')
            loginobj=Employee.objects.get(name=name,contact=contact,place=place)
            if loginobj:
                return render(request,'newhome.html')
            else:
                return render(request,'newlogin.html',{"msg":'invalid username or number'})
        except Exception as e:
                return render(request,'newlogin.html',{"msg":e})  
    return render(request,'newlogin.html')    
def fnnewhome(request):
    return render(request,'newhome.html')
def fnajax(request):
    return render(request,'ajax.html')
def fndelete(request):
    if(request.method=='POST'):
        eid=request.POST.get('id')
        deleteobj=Employee.objects.get(id=eid)
        deleteobj.delete()
        return render(request,'delete.html')
    else:
        return render(request,'delete.html')


@api_view(['GET'])
def fnapidemo(request):
    demo=Apidemo.objects.all()
    demo2=[{'id':i.id,'name':i.name,'contact':i.contact,'place':i.place}for i in demo]
    return JsonResponse({'demo2':demo2})
@api_view(['POST'])
def fnapidemoget(request):
    demo=request.data
    demo2=Apidemo(name=demo['name'],contact=demo['contact'],place=demo['place'])
    demo2.save()
    return Response('Data inserted successfully')
@api_view(['DELETE'])
def fnapidemodelete(request,id):
    demo=Apidemo.objects.get(id=id)
    demo.delete()
    return Response('Data deleted successfully')
@api_view(['POST','PUT'])
def fnapidemoupdate(request,id):
    demo=request.data
    demoupdate=Apidemo.objects.get(id=id)
    demoupdate.name=demo['name']
    demoupdate.save()
    return Response('Data updated successfully')
@login_required()
def fnprofile(request):
    return render(request,'accounts/profile.html')
def fnregister(request):
    f=UserCreationForm(request.POST)
    if f.is_valid():
        f.save()
        return render(request,'new.html')
    return render(request,'register.html',{'form':f})