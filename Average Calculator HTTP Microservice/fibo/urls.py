from django.urls import path
from . import views

urlpatterns = [

    path('',views.fibo(),name="fibo"),

   
]