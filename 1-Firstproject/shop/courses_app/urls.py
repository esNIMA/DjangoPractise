from django.urls import path
from . import views



urlpatterns = [
    path('courses' , views.courses),
    path('detail/<int:id>' , views.course_detail)
]