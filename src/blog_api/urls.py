from django.contrib import admin
from django.urls import path, include
from .views import PostDetail, PostList

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name = 'retrievedestroyupdate'),
    path('', PostList.as_view(), name = 'listcreate'),
]
