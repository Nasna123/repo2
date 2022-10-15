from django.urls import path
from .import views
urlpatterns=[
    path('page1/',views.fun1,name='page1'),
     path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
]