from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    contact_info = {
        "name":"Alimul Razi",
        "phone": "01716463156",
        "email": "alimulrazi28@gmail.com",
        "countrys": ['Bangladesh','United States', 'United Kingdom']
    }
    return render(request,'index.html', contact_info)
    #return HttpResponse( "Welcome to home page")