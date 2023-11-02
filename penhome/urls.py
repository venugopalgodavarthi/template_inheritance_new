from django.urls import path
from penhome.views import home, index, car, student
urlpatterns = [
    path(route='home/', view=home, name="home/"),
    path(route='index/', view=index, name="index/"),
    path(route='car/', view=car, name="car/"),
    path(route='student/<int:pk>/', view=student, name="student/"),
]
