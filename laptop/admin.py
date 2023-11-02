from django.contrib import admin

from laptop.models import laptop, spec
# Register your models here.


class laptop_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'model_no']


class spec_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'model_no', 'ram',
                    'rom', 'processor', 'desc', 'version', 'type_os']


admin.site.register(laptop, laptop_admin)
admin.site.register(spec, spec_admin)
