from django.urls import path
from . import views

#create a url path for any request by django
urlpatterns = [
    path('', views.home),
    path('/signup', views.base)
]
