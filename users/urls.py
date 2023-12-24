"""Определяет схемы url для users"""
from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # Включить URL авторизации по умолчанию
    # в django.contrib.auth.urls содержатся именованные схемы login и logout
    path('', include('django.contrib.auth.urls')),
    # Страница выхода
    path('logout_my/', views.logout_my, name='logout_my'),
    # path('log_out/', views.log_out, name='log_out'),
    # Страница регистрации
    path('register/', views.register, name='register'),
]