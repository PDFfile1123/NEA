from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.Edit, name='Edit'), # attaches the primary key of whichever data you are editting into the path, used by the views.py function to create the right page
]