from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.my_login, name="login"),
    path('logout/', views.my_logout, name="logout"),
    path('register/', views.my_register, name="register"),
]
