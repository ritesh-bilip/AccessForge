from django import urls
from . import views
from django.urls import path

urlpatterns=[
  path('signup/',views.signup,name='signup'),
  path('login/',views.login_user,name='login'),
  path('',views.home,name='home'),
]