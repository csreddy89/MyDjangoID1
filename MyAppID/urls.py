from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.registerPage, name='register'),
    path('loginPage/',views.loginPage,name='login'),
    path('logoutPage/',views.logoutPage,name='logout'),
]