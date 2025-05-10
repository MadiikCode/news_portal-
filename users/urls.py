from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_user_view, name='register'),
    path('sign/', views.sign_user_view, name='sign'),
    path('logout/', views.sign_out_user_view, name='logout'),
]

