from django.shortcuts import render

# Create your views here.

def home(request):
    contact_info = {
        "name":"Alimul Razi",
        "phone": "01716463156",
        "email": "alimulrazi28@gmail.com",
        "countrys": ['Bangladesh','United States', 'United Kingdom']
    }
    return render(request,'index.html', contact_info)