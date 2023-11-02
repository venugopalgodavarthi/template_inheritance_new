from django.db import models

# Create your models here.


class base(models.Model):
    name = models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=[
                              ['MALE', 'MALE'], ['FEMALE', 'FEMALE']])
    email = models.EmailField()
    dob = models.DateField()
    dor = models.DateTimeField(auto_now=True)
    Blood = models.CharField(max_length=5, choices=[['A-', 'A-'], ['A+', 'A+'], ['B-', 'B-'], [
                             'B+', 'B+'], ['O-', 'O-'], ['O+', 'O+'], ['AB-', 'AB-'], ['AB+', 'AB+']])


class student(base):
    class_no = models.CharField(max_length=10)
    cgpa = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    section = models.CharField(max_length=10)


class Teacher(base):
    subject = models.CharField(max_length=10)
    salary = models.PositiveIntegerField()
    year = models.PositiveIntegerField()


class staff(base):
    salary = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
