from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('index.html', views.index),
    path('answer.html', views.get_answer),
]
