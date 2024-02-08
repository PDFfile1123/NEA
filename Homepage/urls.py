from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'), # attaches the path in the main urls file to the Homepage specific path
]