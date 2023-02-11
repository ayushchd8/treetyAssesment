from django.db import models

# Create your models here.
class Company(models.Model):
    Exchange = models.CharField(max_length=100, null=True, blank=True)
    Symbol = models.CharField(max_length=100, null=True,blank=True)
    Shortname = models.CharField(max_length=250, null=True,blank=True)
    Longname = models.CharField(max_length=250, null=True,blank=True)
    Sector = models.CharField(max_length=250, null=True,blank=True)
    Industry = models.CharField(max_length=250, null=True,blank=True)
    Currentprice = models.FloatField(max_length=250, null=True,blank=True)
    Marketcap = models.IntegerField(max_length=250, null=True,blank=True)
    Ebitda = models.IntegerField(max_length=250, null=True,blank=True)
    Revenuegrowth = models.FloatField(max_length=50, null=True,blank=True)
    City = models.CharField(max_length=100, null=True,blank=True)
    State = models.CharField(max_length=50, null=True,blank=True)
    Country = models.CharField(max_length=50, null=True,blank=True)
    Fulltimeemployees = models.IntegerField(max_length=50, null=True,blank=True)
    Longbusinesssummary = models.CharField(max_length=2000, null=True,blank=True)
    Weight = models.FloatField(max_length=250, null=True,blank=True)
