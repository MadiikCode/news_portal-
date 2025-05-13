from django.urls import path
from . import views

app_name = 'news'


urlpatterns = [
    path('', views.news_list, name='news'),
   # path('news/detail/<int:pk>/', views.news_detail, name='news_detail2'),
  #  path('news/create/', views.news_create, name='news_create'),
   # path('', views.NewsListView.as_view(), name='news')
    path('new-detail/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    #path('create/<slug:category_slug>/', views.news_create_view, name='news_create'),
    path('create/', views.news_create_view, name='create'),  # Без категории
    path('<slug:category_slug>/create/', views.news_create_view, name='create_with_category'),
    path('new-update/<int:pk>', views.NewsUpdateView.as_view(), name='update'),
    path('new-delete/<int:pk>', views.NewsDeleteView.as_view(), name='delete'),
    path('categories/', views.category_list, name='category_list'),  # добавь этот путь
    path('add-category/', views.add_category, name='add_category'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),

]
