from companies.models import Company
import csv

def run():
    with open('companies/sp500_companies.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        # Company.objects.all().delete()

        for row in reader:
            # print(row)
            

            Exchange,Symbol,Shortname,Longname,Sector,Industry,Currentprice,Marketcap,Ebitda,Revenuegrowth,City,State,Country,Fulltimeemployees,Longbusinesssummary,Weight = row
            if Ebitda == "" :
                Ebitda = None

            if State=="":
                State= None

            if  Country=="":
                 Country=None
            
            if Fulltimeemployees=="":
                Fulltimeemployees=None

            if Revenuegrowth=="":
                Revenuegrowth=None

            obj = Company(Exchange=Exchange, Symbol=Symbol, Shortname=Shortname,
                          Longname=Longname,Sector=Sector,Industry=Industry,
                          Currentprice=Currentprice,Marketcap=Marketcap,
                          Ebitda=Ebitda,Revenuegrowth=Revenuegrowth,
                          City=City,State=State,Country=Country,
                          Fulltimeemployees=Fulltimeemployees,Longbusinesssummary=Longbusinesssummary,
                          Weight=Weight)
            obj.save()