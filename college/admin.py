from django.contrib import admin
from college.models import staff, student, faculty
# Register your models here.


class student_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'address', 'gender',
                    'dob', 'dor', 'Blood', 'branch', 'class_no', 'cgpa', 'year']


class faculty_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'address', 'gender',
                    'dob', 'dor', 'Blood', 'branch', 'subject', 'salary', 'year', 'design']


class staff_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'address', 'gender',
                    'dob', 'dor', 'Blood', 'branch', 'salary', 'year']


admin.site.register(student, student_admin)
admin.site.register(staff, staff_admin)
admin.site.register(faculty, faculty_admin)
