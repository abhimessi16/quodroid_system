from django.urls import path
from . import views

urlpatterns = [
    path("execute/", views.run_robot_test, name='Run robot tests')
]