from django.db import models

# Create your models here.


class customer(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()


class product(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveSmallIntegerField()
    ex_date = models.DateField()


class sells(customer, product):
    sid = models.AutoField(primary_key=True)
    dor = models.DateTimeField(auto_now=True)
    gst = models.CharField(max_length=50)
    shipping_address = models.TextField()
