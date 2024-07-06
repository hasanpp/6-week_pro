from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('admin/home/', views.admin_home, name='admin_home'),
    path('admin/delete/<int:user_id>/', views.admin_delete_user, name='admin_delete_user'),
    path('admin/edit/<int:user_id>/', views.admin_edit_user, name='admin_edit_user'),
    path('admin_signout', views.admin_signout, name='admin_signout'),
    path('admin/create_user', views.create_user, name='create_user'),
]
