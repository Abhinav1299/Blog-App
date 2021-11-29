from django.contrib import auth
from django.http import response
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from blog.models import Post, Category
from rest_framework import status
from django.urls import reverse



# TESTING APIs
class PostTest(APITestCase):

    # test for checking 'all post retrieve' functionality
    def testPostView(self):
        url = reverse('blog_api:listcreate')                # blog_api --> app name, listcreate --> postlist view (reverse is creating our api endpoint)
        response = self.client.get(url, format = 'json')    # client simulates browser request
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test for checking 'create post' functionality
    def testPostCreate(self):
        cat = Category.objects.create(name = 'django')
        user = User.objects.create_user(username = 'testing', password = 'testing')
        data = { 
            'title' : 'testpost', 
            'author' : 1,
            'content' : 'testing post', 
            'excerpt' : 'testing post', 
            'slug' : 'testing-post',
            'post_status' : 'published',
            }

        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
