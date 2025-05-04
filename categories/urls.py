from django.urls import path
from . import views




urlpatterns = [
    path('logout/', views.custom_logout, name='logout'),
    path('', views.category_list, name='category_list'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('add/', views.category_add, name='category_add'),
]