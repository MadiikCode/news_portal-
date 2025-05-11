from django.urls import path
from . import views



app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('sign/', views.user_sign_view, name='sign'),
    # path('login/', views.user_sign_view, name='login'),
   # path('logout/', views.sign_out_user_view, name='logout'),
]

