from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import *


app_name = "accounts"

urlpatterns = [
    path('', views.login_user , name='login'),
    path('logout/', views.logout_user , name='logout'),
    
    path('change_password/', views.change_password, name='change_password'),
    
    # path('password_change/', auth_views.PasswordChangeView.as_view() , name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    
]
