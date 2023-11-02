from django.contrib import admin

from school.models import base, staff, student, Teacher
# Register your models here.


class base_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'address', 'gender',
                    'dob', 'dor', 'Blood']


class student_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'address', 'gender',
                    'dob', 'dor', 'Blood', 'section', 'class_no', 'cgpa', 'year']


class Teacher_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'address', 'gender',
                    'dob', 'dor', 'Blood', 'subject', 'salary', 'year']


class staff_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'address', 'gender',
                    'dob', 'dor', 'Blood', 'salary', 'year']


admin.site.register(base, base_admin)
admin.site.register(student, student_admin)
admin.site.register(staff, staff_admin)
admin.site.register(Teacher, Teacher_admin)
