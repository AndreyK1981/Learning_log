"""Определяет схемы url для learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # При пересылке из learning_log/urls.py проект перебирает эти адреса по порядку
    # Домашняя страница
    path('', views.index, name='index'),
    # path('index/', views.index, name='index'), # Меняет путь HTML
    # Страница со списком всех тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    # идентификатор topic_id отправляет номер функции представления views.topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница (форма) для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница (форма) для добавления новой записи
    # идентификатор topic_id отправляет номер функции представления views.new_entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    # идентификатор entry_id отправляет номер функции представления views.edit_entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]