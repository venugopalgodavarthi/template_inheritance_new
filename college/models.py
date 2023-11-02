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
    branch = models.CharField(max_length=10,
                              choices=[['CSE', 'CSE'], ['ECE', 'ECE'], ['EEE', 'EEE'], ['CIVIL', 'CIVIL'], ['MECH', 'MECH'], ['ONLINE', 'ONLINE']])

    class Meta:
        abstract = True


class student(base):
    class_no = models.CharField(max_length=10)
    cgpa = models.PositiveIntegerField()
    year = models.PositiveIntegerField()


class faculty(base):
    subject = models.CharField(max_length=10)
    salary = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    design = models.CharField(max_length=50)


class staff(base):
    salary = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
