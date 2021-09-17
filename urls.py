"""firstwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Myapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hi,name='Hi'),
    path('hello/',views.hello,name='hello'),
    path('hi1/<str:val>',views.hi1,name='hi1'),
    path('rollno/<int:num>',views.rollno,name='rollno'),
    path('details/<str:val>/<int:rollno>,views.details'),
    path('sample/',views.home,name='')
]

