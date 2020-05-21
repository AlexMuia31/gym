from django.urls import path
from . views import  BlogView
from . models import Blog

urlpatterns= [
    path('', BlogView.as_view(template_name='blog/blog.html'))

]