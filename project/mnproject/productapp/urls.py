from django.conf import urls
from django.urls import path
from . import views


app_name = 'productapp'
urlpatterns = [
    path('products/', views.products, name='products'),
    path('basket/', views.basket, name ='basket'),
    path('', views.home, name='home'),
    path('/basket/<str:id>/', views.addtobasket, name='addtobasket'),
    path('basket/<str:id>/', views.removefrombasket, name='removefrombasket'),
    # path('basket/', views.basket_total, name='basket_total')
]
