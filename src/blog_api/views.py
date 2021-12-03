from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, BasePermission, IsAuthenticatedOrReadOnly


# Creating custom permission so that users which created the post are the only one who can 
# update or delete it.

class PostAuthorWritePermission(BasePermission):
    message = 'Editing Posts is restricted to the author of the post only.'

    def has_object_permission(self, request, view, obj):        # object level permission
        # read requests
        if request.method in SAFE_METHODS:
            return True
        
        # write requests
        else:
            if obj.author == request.user:
                return True
            else:
                return False

class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]                        # view level permission --> overriding project level permissions
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostAuthorWritePermission):
    permission_classes = [PostAuthorWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer