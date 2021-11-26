from django.contrib import admin
from django.urls import path, include
from .views import postDetail, postList

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', postDetail.as_view(), name = 'detailcreate'),
    path('', postList.as_view(), name = 'listcreate'),
]
