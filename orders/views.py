from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views import generic, View
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import OrdersForm
from .models import Orders, Merchant, District, Division,SubDistrict
import json
def createOrder(request):
    marchant= Merchant.objects.all().order_by('name')
    marchant_list=list(marchant.values('name'))

    subdistrict=SubDistrict.objects.all().order_by('name')
    sub_list=list(subdistrict.values('name','district__name'))

    district=District.objects.all().order_by('name')
    district_list=list(district.values('name','division__name'))

    if request.method == 'POST':
        name=request.POST['name']
        marchant=Merchant.objects.get(name=name)
        marchant_invoice_id=request.POST['marchant_invoice_id']
        location=request.POST['location']
        product_type=request.POST['product_type']
        location_type=request.POST['location_type']
        weight=request.POST['weight']
        price=request.POST['price']
        with_cod=request.POST['with_cod']
        with_return=request.POST['with_return']
        # final_price=request.POST['final_Price']
        district=request.POST['district']
        dis=District.objects.get(name=district)

        subdistrict=request.POST['subdistrict']
        print(subdistrict)
        subdis=SubDistrict.objects.get(name=subdistrict)

        Orders.objects.create(marchant=marchant,marchant_invoice_id=marchant_invoice_id,location=location,product_type=product_type,location_type=location_type,weight=weight,price=price,price_with_return_charges=with_return,price_with_cod=with_cod,subdistrict=subdis, district=dis)
        
        messages.success(request, 'Successfully Ordered.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = OrdersForm()
    context = {
        'form': form,
        'marchant':json.dumps(marchant_list),
        'district_list':json.dumps(district_list),
        'sub_list':json.dumps(sub_list),
        'mar':marchant,
        'district':district
    }
    return render(request, 'orders/createorder.html', context)

from .r import dson,upozila
# def district(request):
#     for d in dson:
#         if  not Division.objects.filter(name=d).exists():
#             division=Division.objects.create(name=d)
#         for i in dson[d]:
#             division=Division.objects.get(name=d)
#             if not District.objects.filter(name=i).exists():
#                 District.objects.create(name=i, division=division)
#     messages.success(request, "All District Added to the Database! No Need to click again")
#     return render(request, 'accounts/home.html')
def upozilas(request):
    for data in upozila:
        if  not Division.objects.filter(name=data["division"]).exists():
            division=Division.objects.create(name=data["division"])
        else:
            division=Division.objects.get(name=data["division"])
        if  not District.objects.filter(name=data["district"]).exists():
            district=District.objects.create(name=data["district"],division=division)
        else:
            district=District.objects.get(name=data["district"])
        if  not SubDistrict.objects.filter(name=data["upazila"]).exists():
            upazila=SubDistrict.objects.create(name=data["upazila"],district=district)
    messages.success(request, "All SubDistrict Added to the Database! No Need to click again")
    return render(request, 'accounts/home.html')
    
class OrderList(generic.ListView):
    model = Orders
    template_name='orders/orderlist.html'
    context_object_name = 'orders'

    
    
    