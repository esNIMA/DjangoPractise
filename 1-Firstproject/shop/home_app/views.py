from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hi this is my Home page")

def contactUs(request): 
    return HttpResponse("Hi this is Contact us page")
