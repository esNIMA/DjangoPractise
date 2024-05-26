from django.shortcuts import render, HttpResponse

users_list = [
    {'name' : "Nima" , 
     "lastName" : "Mahmoodian",
     "phoneNumber":"09387414233",
     "City": "Esfahan"},
    {'name' : "ali" , 
     "lastName" : "Mahmoodian",
     "phoneNumber":"09325886576",
     "City": "Esfahan"},
    {'name' : "Erfan" , 
     "lastName" : "Mahmoodian",
     "phoneNumber":"09374927630",
     "City": "Esfahan"},
    {'name' : "Hamid" , 
     "lastName" : "Mahmoodian",
     "phoneNumber":"09365901423",
     "City": "Esfahan"},
]



# Create your views here.
def profile(request, username):
    return render(request , "accounts_app/profile.html" , {"name" : username})

def info(request):
    return render(request , "accounts_app/info.html")

def users(request):
    return render(request , "accounts_app/user.html" , {"users_list": users_list})
