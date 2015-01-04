from django.contrib import admin
from IrishFashionBuyer.models import OrderDetails
from IrishFashionBuyer.models import Order



# Register your models here.
class OrderDetailsInline(admin.StackedInline):
    model = OrderDetails
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['order_number']}),
        ('Order Information', {'fields':['order_time','total_price','total_original_price','total_weight','delivery_address','delivery_number','order_paid','order_user','order_comments']}),
    ]
    inlines = [OrderDetailsInline]

admin.site.register(Order, OrderAdmin)





