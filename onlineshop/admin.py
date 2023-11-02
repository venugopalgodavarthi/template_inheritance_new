from django.contrib import admin
from onlineshop.models import customer, sells, product
# Register your models here.


class customer_admin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'address', 'phone', 'email']


class product_admin(admin.ModelAdmin):
    list_display = ['pid', 'pname', 'desc', 'price', 'quantity', 'ex_date']


class sells_admin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'address', 'phone', 'email', 'pid',
                    'pname', 'desc', 'price', 'quantity', 'ex_date', 'gst', 'dor', 'shipping_address']


admin.site.register(customer, customer_admin)
admin.site.register(product, product_admin)
admin.site.register(sells, sells_admin)
