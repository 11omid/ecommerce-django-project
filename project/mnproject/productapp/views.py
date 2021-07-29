from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Products, Basket
from django.template import RequestContext
from django.http import HttpResponseRedirect

#Products Html
def products(request):
    products_list = Products.objects.order_by('-pub_date')
    context = {'products_list': products_list,'title': "Products"}
    return render(request, 'productapp/products.html', context)

#Basket Html
def basket(request):
    basket_list = Basket.objects.order_by('-pub_date')
    #total price of the basket items
    total = sum([item.get_total for item in basket_list])
    context = {'basket_list': basket_list, 'total':total,'title': "Basket"}
    return render(request, 'productapp/basket.html', context)

#Home page Html
def home(request):
    products_list = Products.objects.order_by('-pub_date')
    basket_list = Basket.objects.order_by('-pub_date')
    context = {'products_list': products_list,'basket_list': basket_list,'title': "Home"}
    return render(request, 'pages/index.html', context)

#Rendering Images for products
def image(request):
    images = Products()
    variables = RequestContext(request,{'product_pic':images})
    return render(None,'image.html',variables)

#adding products items to basket
def addtobasket(request, id):
    if request.method == 'POST':
        product = Products.objects.get(id=id)
        basket, created = Basket.objects.get_or_create(products=product)
        basket.amount=request.POST['amount']
        basket.save()
        return HttpResponseRedirect(reverse("productapp:basket"))

#removing items from basket
def removefrombasket(request, id):
    if request.method == 'POST':
        product = Basket.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect(reverse("productapp:basket"))
