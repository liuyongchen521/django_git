
from django.urls import path
from book_app import views #导入视图文件
urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('reg/', views.register),
]
