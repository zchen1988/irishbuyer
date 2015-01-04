from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Order(models.Model):
    def __str__(self):
        return self.order_number+' -> '+str(self.order_time)
    order_number = models.CharField(max_length=500)
    order_time = models.DateTimeField()
    total_price = models.CharField(max_length=200,default='0')
    total_original_price = models.CharField(max_length=200,default='0')
    total_weight = models.CharField(max_length=200,default='0')
    delivery_address = models.CharField(max_length=500,default='Please insert')
    delivery_number = models.CharField(max_length=500,default='Not available')
    order_paid = models.BooleanField(default=None)
    order_user = models.ForeignKey(User)
    order_comments = models.CharField(blank=True,max_length=2000,default='No Comments')



class OrderDetails(models.Model):
    def __str__(self):
        return self.order_number+' - '+self.product_name
    order = models.ForeignKey(Order)
    order_number = models.CharField(max_length=500)
    product_name = models.CharField(max_length=200)
    order_time = models.DateTimeField()
    product_price = models.FloatField()
    product_original_price = models.FloatField()
    product_desc = models.CharField(max_length=500)
    product_purchased = models.BooleanField(default=None)
    product_weight = models.FloatField()
    product_quantity = models.IntegerField()
