from django.db import models

class Products(models.Model):
    products_name = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    note = models.CharField(max_length=200)
    inventory = models.IntegerField(default=1)
    product_pic = models.ImageField(upload_to ='images/', default='images/broken/broken.png')

    def __str__(self):
        if (self.inventory<=0):
            return self.products_name + ' (Out of Stock)'
        return self.products_name

class Basket(models.Model):
    products = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=1)


    def __str__(self):
        return str(self.products)

    #price of a item with amount>1
    @property
    def get_total(self):
        total = self.products.price * self.amount
        return total

    #price of a item in basket from products
    def get_price(self):
        price = self.products.price
        return price
