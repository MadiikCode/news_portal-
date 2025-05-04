from django.urls import path
from . import views



urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail2, name='news_detail2'),
]
