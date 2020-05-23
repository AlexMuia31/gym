from django.shortcuts import render
from django.views.generic import ListView ,DetailView, UpdateView,CreateView
from . models import User, contactModel
from django.contrib.messages.views import SuccessMessageMixin  #using this to send display success message

# Create your views here.
class Home(ListView):
    model= User
    template_name='core/home.html'

class AboutView(ListView):
    model= User
    template_name='core/about.html'

class ContactUs(SuccessMessageMixin, CreateView):
    model= contactModel
    fields=('name','Email','message')
    template_name='core/contact.html'
    success_url ="/core/contact"   #redirects to home after submiting the message

    def get_success_message(self,cleaned_data):
        return "Message sent successfully"

