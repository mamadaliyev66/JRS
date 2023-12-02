from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("upload/", views.upload_pdf, name="upload"),
    path("upload/result/", views.result, name="result")
]
