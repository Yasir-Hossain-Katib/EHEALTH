from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name="myapp"),

    path('index/',views.index,name="index"),
    
    path('register/',views.register,name="register"),

    path('login/',views.loginP,name="login"),

    path('logout/',views.logoutU,name="logout"),

    path('doctorSignUp/', views.doctorSignUp, name='doctorSignUp'),

    

    path('doctorLogin/', views.loginD, name='doctorLogin'),

    path('doctorProfile/', views.doctorProfile, name='doctorProfile'),

    path('bio/', views.bio, name='bio'),

    path('payment/', views.payment, name='payment'),

    path('success/', views.success, name='success'),

    path('Pboard/', views.Pboard, name='Pboard'),

    path('Dboard/', views.Dboard, name='Dboard')

    

    
] 