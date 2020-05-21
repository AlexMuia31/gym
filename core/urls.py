from django.urls import path
from django.conf.urls import url
from .views import AboutView, ContactUs
from .models import User

app_name='core'

urlpatterns=[
    path('about/', AboutView.as_view(), name='about'),
    path('contact/',ContactUs.as_view(), name='contact')
]