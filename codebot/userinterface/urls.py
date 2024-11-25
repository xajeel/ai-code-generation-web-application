
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('suggest/', views.suggest, name='suggest'),
    path('register/', views.registration, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('history', views.history, name='history'),
    path('delete/<code_id>', views.delete, name='delete'),
    path('about', views.about, name='about')
]
