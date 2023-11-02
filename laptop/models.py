from django.db import models

# Create your models here.


class laptop(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    model_no = models.CharField(max_length=50)


class spec(laptop):
    rom = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    processor = models.CharField(max_length=20)
    version = models.CharField(max_length=20)
    type_os = models.CharField(max_length=20, choices=[
                               ['WINDOWS', 'WINDOWS'], ['UNIX', 'UNIX'], ['MAC', 'MAC']])
    desc = models.TextField()
