from django.urls import path
from . import views
from .views import CategoryCreateView, CategoryUpdateView
from .views import category_create





urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('<slug:slug>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('create/', category_create, name='category_create'),  # Ручная обработка
]
