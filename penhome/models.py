from django.db import models

# Create your models here.


class student_model(models.Model):
    sid = models.PositiveIntegerField(primary_key=True)
    sname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField(unique=True)
    marks = models.PositiveIntegerField()

    def __str__(self):
        return str(self.sid)+'__'+self.sname


class subject_model(models.Model):
    subid = models.AutoField(primary_key=True)
    science = models.BooleanField()
    social = models.BooleanField()
    maths = models.BooleanField()
    sid = models.ForeignKey(student_model, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.subid)


class car_model(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    series = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=20, choices=[['Red', 'RED'], [
                             'Blue', 'BLUE'], ['White', 'WHITE'], ['Black', 'BLACK']])
    valid = models.PositiveIntegerField()
    brand = models.CharField(max_length=50)
    ins = models.BooleanField()
    warranty = models.PositiveIntegerField()
