from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Tender
from authentication.decorators import allowed_users
from .filters import TenderFilters


# Create your views here.
def ListOfTenders(request):

    tenders=Tender.objects.all()


    myFilter= TenderFilters(request.GET, queryset=tenders)
    tenders=myFilter.qs
    
    return render(request,"authentication/tender.html",{
        'tenders':tenders,'myFilter':myFilter
    })
@allowed_users(allowed_roles=['admin','add group'])
def AddTenders(request):
    if request.method=="POST":
        if request.POST.get('tender_date','tender_active')=="":
            return render(request, "authentication/add_tenders.html",{'error':True}) 
        # data fetch
        hospital_name=request.POST.get("hospital_name")
        tender_number=request.POST.get("tender_number")
        product_name=request.POST.get("product_name")
        hospital_location=request.POST.get("hospital_location")
        hospital_remarks=request.POST.get("hospital_remarks")
        tender_winner=request.POST.get("tender_winner")
        tender_price=request.POST.get("tender_price")
        tender_date=request.POST.get("tender_date")
        tender_active=request.POST.get("tender_active")
        
        # create model object and set the data
        t=Tender()
        t.Hospital=hospital_name
        t.Tender_number=tender_number
        t.Product=product_name
        t.Location=hospital_location
        t.Remarks=hospital_remarks
        t.Tender_Won_By=tender_winner
        t.Winning_Price=tender_price
        t.Date=tender_date
        if tender_active is None:
            t.Active=False
        else:
            t.Active=True
        
        # save the object
        t.save()
        # prepare msg
        # print("data is coming")
        return redirect("/tender/")
    return render(request, "authentication/add_tenders.html",{})

@allowed_users(allowed_roles=['admin'])
def delete_tender(request, tender_number):
    tender=Tender.objects.get(pk=tender_number)
    tender.delete()
    return redirect(ListOfTenders)

@allowed_users(allowed_roles=['admin'])
def update_tender(request, tender_number):
    tender=Tender.objects.get(pk=tender_number)
    return render(request,"authentication/update_tender.html",{'tender': tender})

@allowed_users(allowed_roles=['admin','add group'])
def do_update_tender(request, tender_number):
    if request.method=="POST":
        # data fetch
        hospital_name=request.POST.get("hospital_name")
        tender_number_id=request.POST.get("tender_number")
        product_name=request.POST.get("product_name")
        hospital_location=request.POST.get("hospital_location")
        hospital_remarks=request.POST.get("hospital_remarks")
        tender_winner=request.POST.get("tender_winner")
        tender_price=request.POST.get("tender_price")
        tender_date=request.POST.get("tender_date")
        tender_active=request.POST.get("tender_active")

        t=Tender.objects.get(pk=tender_number)
        t.Hospital=hospital_name
        t.Tender_number=tender_number_id
        t.Product=product_name
        t.Location=hospital_location
        t.Remarks=hospital_remarks
        t.Tender_Won_By=tender_winner
        t.Winning_Price=tender_price
        t.Date=tender_date
        if tender_active is None:
            t.Active=False
        else:
            t.Active=True
        # save the object
        t.save()

    return redirect("/tender/")
