from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout")

]
