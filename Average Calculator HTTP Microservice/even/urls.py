from django.urls import path
from . import views

urlpatterns = [
    #genres - home page
    path('',views.even(),name="even"),
    # genre/1 collection 1 
    path('<pk>',views.details.as_view(),name="details"),
    # genre / register
    path('register/',views.UserFormView.as_view(),name="UserForm")

   
]