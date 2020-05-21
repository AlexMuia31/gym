from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from . models import User

# Create your views here.
class Home(ListView):
    model= User
    template_name='core/home.html'

class AboutView(ListView):
    model= User
    template_name='core/about.html'

class ContactUs(ListView):
    model= User
    template_name='core/contact.html'
    
