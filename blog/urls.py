from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_All_Blogs,name="get_All_Blogs"),
    path('create/', views.create_BLog,name="create_Blog"),
    path('<int:blogId>/edit/', views.edit_Blog,name="edit_Blog"),
    path('<int:blogId>/delete/', views.delete_Blog,name="delete_Blog"),
    path('register/', views.register, name="register"),
]
