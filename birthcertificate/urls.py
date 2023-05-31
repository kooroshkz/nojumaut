from django.urls import path
from . import views # . means from currect directory

urlpatterns = [
    path("", views.index, name="index")
]
