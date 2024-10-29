from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.home),
   path('register/', views.register_page, name='register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
     path('about/',views.about),
]