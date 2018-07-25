"""
URL routing schema for first-task.

"""

from django.urls import path

from . import views

app_name = "first-task"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
