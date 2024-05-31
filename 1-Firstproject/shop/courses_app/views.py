from django.shortcuts import render
from .models import Course
# Create your views here.


def courses(request):
    courses = Course.objects.all()
    return render(request, "courses_app/courses.html", {"courses": courses})


def course_detail(request, id, views): 
    course = Course.objects.get(id= id)
    views = Course.objects.update()
    return render(request, "courses_app/course_detail.html", {"course" : course})
