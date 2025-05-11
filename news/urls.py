from django.urls import path
from . import views



urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('news/detail/<int:pk>/', views.news_detail, name='news_detail2'),
    path('news/create/', views.news_create, name='news_create'),

]
