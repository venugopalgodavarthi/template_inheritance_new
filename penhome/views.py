from django.shortcuts import render
from penhome.models import car_model, student_model, subject_model
from django.db.models import Min, Max, Count, Avg, Sum
# Create your views here.


def home(request):
    return render(request=request, template_name='home.html')


def index(request):
    return render(request=request, template_name='index.html')


def car(request):
    data = car_model.objects.all().order_by('-name')
    return render(request=request, template_name="car.html", context={'data': data})


def student(request, pk):
    data = student_model.objects.filter(sid=pk)
    # temp = subject_model.objects.filter(subid=(subject_model.objects.filter(sid=pk).aggregate(Max('subid'))['subid__max']))

    
    temp = subject_model.objects.filter(sid=pk).order_by('-subid')
    print(temp)
    return render(request=request, template_name="student.html", context={'data': data, 'subject': temp})


# orderby
# ascending order
# data = car_model.objects.all().order_by('name')


# descending order
# data = car_model.objects.all().order_by('-name')


# multi row
# from django.db.models import Max,Min,Avg,Sum,Count

#  data = car_model.objects.all().aggregate(Sum('price'))    ===>{'Price__Sum': value}

# data = car_model.objects.all().aggregate(Max('price'))    ===>{'Price__Max': value}

# data = car_model.objects.all().aggregate(Min('price'))    ===>{'Price__Min': value}

# data = car_model.objects.all().aggregate(Count('price'))    ===>{'Price__Count': value}

# data = car_model.objects.all().aggregate(Avg('price'))    ===>{'Price__Avg': value}

# data['Price__sum']   ==> value


# like

# Sql query
# select * from car where color like "Blue";

# ORM code
# car_model.objects.filter(color__exact='Blue')
# car_model.objects.filter(color__iexact='Blue')


# Sql query
# select * from car where color like "%l%";

# ORM code
# car_model.objects.filter(color__contains='B')
# car_model.objects.filter(color__icontains='B')


# Sql query
# select * from car where color like "B%";

# ORM code
# car_model.objects.filter(color__startswith='B')
# car_model.objects.filter(color__istartswith='B')

# Sql query
# select * from car where color like "B%";

# ORM code
# car_model.objects.filter(color__endswith='k')
# car_model.objects.filter(color__iendswith='k')


# Sql query
# select * from car where cid in [1,2,3];

# ORM code
# car_model.objects.filter(cid__in=[1,2,3])


# Sql query
# select * from car where cid not in [1,2,3];

# ORM code
# car_model.objects.exclude(cid__in=[1,2,3])


# Sql query
# select * from car where cid between (10,90);

# ORM code
# car_model.objects.filter(cid__range=(10,90))


# Sql query
# select * from car where cid not between (10,90);

# ORM code
# car_model.objects.exclude(cid__range=(10,90))


# data = car_model.objects.all().values_list()

# relational operators
# greater than
# car_model.objects.filter(price__gt=3500000).values_list()

# greater or equalto than
# car_model.objects.filter(price__gte=3500000).values_list()


# less than
# car_model.objects.filter(price__lt=3500000).values_list()

# less or equalto than
# car_model.objects.filter(price__lte=3500000).values_list()

# equal
# car_model.objects.filter(price=3500000).values_list()
# (or)car_model.objects.filter(price__exact=3500000).values_list()

# not equal
# car_model.objects.exclude(price=3500000).values_list()
# car_model.objects.exclude(price__exact=3500000).values_list()


# Sql query
# select * from car where price=3500000 & color='Blue';

# ORM CODE
# data = car_model.objects.filter(price=3500000, color='Blue')   # (or)

# data = car_model.objects.filter(price=3500000) & car_model.objects.filter(color='Blue') # (or)

# data = car_model.objects.filter(Q(price=3500000) & Q(color='Blue'))


# Sql query
# select * from car where not(price=3500000 & color='Blue');

# ORM CODE

# data = car_model.objects.exclude(price=3500000, color='Blue')     #(or)

# data = car_model.objects.exclude(price=3500000) & car_model.objects.exclude(color='Blue')    #(or)

# data = car_model.objects.filter(~Q(price=3500000) & ~Q(color='Blue'))


# Sql query
# select * from car where price=3500000 & color!='Blue';

# ORM CODE
# data = car_model.objects.filter(price=3500000) & car_model.objects.exclude(color='Blue') & car_model.objects.exclude(cid=1)

# data = car_model.objects.filter(Q(price=3500000) & ~Q(color='Blue'))


# data = car_model.objects.filter(price=3500000) & car_model.objects.exclude(color='Blue') & car_model.objects.exclude(cid=1)


# Sql query
# select * from car where price=3500000 or color='Red';

# ORM CODE

# data = car_model.objects.filter(price=3500000) | car_model.objects.filter(color='Blue') # (or)

# data = car_model.objects.filter(Q(price=3500000) | Q(color='Blue'))


# Sql query
# select * from car where not(price!=3500000 or color!='Blue');

# ORM CODE

# data = car_model.objects.exclude(price=3500000) | car_model.objects.exclude(color='Blue')    #(or)

# data = car_model.objects.filter(~Q(price=3500000) | ~Q(color='Blue'))

# logical NOT

# Sql query
# select * from car where price!=3500000;

# ORM CODE

# data = car_model.objects.exclude(price=3500000)
# data = car_model.objects.filter(~Q(price=3500000))


# like

# Sql query
# select * from car where color like "Blue";
