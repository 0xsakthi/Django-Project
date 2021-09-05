from django.urls import path
from returning.views import main,perfect,register

urlpatterns = [
    path('',main,name="home"),
    path('sakthi',perfect,name="perfect"),
    path('register',register,name="register")
]
#ALLOWED_HOSTS = ['dc64-157-49-77-2.ngrok.io']