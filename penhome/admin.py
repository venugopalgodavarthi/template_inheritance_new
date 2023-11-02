from django.contrib import admin

# Register your models here.
from penhome.models import car_model, subject_model, student_model


class student_admin(admin.ModelAdmin):
    list_display = ['sid', 'sname', 'email', 'phone', 'marks']


admin.site.register(student_model, student_admin)


class subject_admin(admin.ModelAdmin):
    list_display = ['subid', 'sid', 'social', 'science', 'maths']


admin.site.register(subject_model, subject_admin)


class admin_car(admin.ModelAdmin):
    list_display = ['cid', 'name', 'desc', 'series', 'price',
                    'color', 'valid', 'brand', 'ins', 'warranty']


admin.site.register(car_model, admin_car)
