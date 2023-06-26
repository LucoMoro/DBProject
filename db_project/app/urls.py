from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home),
    path ('contattaci', views.contattaci),
]