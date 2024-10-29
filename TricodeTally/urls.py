
from django.contrib import admin
from django.urls import path,include
from home.views import contact_us,problems
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('problems/',problems,name='problems'),
    path('contact/', contact_us, name='contact_us'),
    path('home/',include('home.urls')),  
    path('donate/',include('donate.urls')),
]
