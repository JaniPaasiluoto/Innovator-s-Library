from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from store.views import *

urlpatterns = [
    path('', index, name="index"),
    url(r'^signup/$', signup, name='signup'),
    
]
