from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('contact/', views.contact, name='employee.contact'),
    #path('service/', views.service, name='employee.service'),
]