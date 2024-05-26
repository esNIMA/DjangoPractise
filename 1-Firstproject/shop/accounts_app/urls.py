from django.urls import path
from . import views

urlpatterns = [
    path('info' , views.info),
    path('users', views.users),
    path('<username>' , views.profile),
]