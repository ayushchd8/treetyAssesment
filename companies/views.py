from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Company
from django.shortcuts import render
from django.template import loader
import csv

def abc(request):
    return redirect("/home/")

def home(request):
    
    return render(request,'home.html')

def companies(request):
    obj = Company.objects.all()
    print(obj)
    context={
        "title" : "company data",
        "obj" : obj
    }
    return render(request,'CompanyList.html',context)

def addcompany(request):
    
    return render(request,'addcompany.html')

def savecompany(request):
    if request.method=="POST":
       form = request.POST
       Exchange=form.get("Exchange")
       Symbol=form.get("Symbol")
       Shortname=form.get("Shortname")
       Longname=form.get("Longname")
       Sector=form.get("Sector")
       Industry=form.get("Industry")
       Currentprice=form.get("Currentprice")
       print('current',Currentprice)
       Marketcap=form.get("Marketcap")
       Ebitda=form.get("Ebitda")
       Revenuegrowth=form.get("Revenuegrowth")
       City=form.get("City")
       State=form.get("State")
       Country=form.get("Country")
       Fulltimeemployees=form.get("Fulltimeemployees")
       Longbusinesssummary=form.get("Longbusinesssummary")
       Weight=form.get("Weight")
       


    if Ebitda == "" :
        Ebitda = None

    if Currentprice == "" :
        Currentprice = None

    if Marketcap == "" :
        Marketcap = None

    if State=="":
        State= None

    if  Country=="":
        Country=None
    
    if Fulltimeemployees=="":
        Fulltimeemployees=None

    if Revenuegrowth=="":
        Revenuegrowth=None

    if Weight=="":
        Weight=None

       
    obj = Company(Exchange=Exchange, Symbol=Symbol, Shortname=Shortname,
                        Longname=Longname,Sector=Sector,Industry=Industry,
                        Currentprice=Currentprice,Marketcap=Marketcap,
                        Ebitda=Ebitda,Revenuegrowth=Revenuegrowth,
                        City=City,State=State,Country=Country,
                        Fulltimeemployees=Fulltimeemployees,Longbusinesssummary=Longbusinesssummary,
                        Weight=Weight)
    obj.save()
    return render(request,'home.html')
