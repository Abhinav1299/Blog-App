from django.contrib import auth
from django.http import response
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from blog.models import Post, Category
from rest_framework import status
from django.urls import reverse


# TESTING APIs
class PostTest(APITestCase):

    # test for checking 'all post retrieve' functionality
    def testPostView(self):
        url = reverse('blog_api:listcreate')                        # blog_api --> app name, listcreate --> postlist view (reverse is creating our api endpoint)
        response = self.client.get(url, format = 'json')            # client simulates browser request
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test for checking 'create post' functionality
    def testPostCreate(self):
        self.cat = Category.objects.create(name = 'django')
        self.user = User.objects.create_user(username = 'testing', password = 'testing')

        self.client.login(username = 'testing', password = 'testing')

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

    # test for checking 'update post' functionality
    def testPostUpdate(self):

        client = APIClient()                # for logging In a user
        self.cat = Category.objects.create(name = 'django')
        self.user1 = User.objects.create_user(username = 'user1', password = 'user1')
        self.user2 = User.objects.create_user(username = 'user2', password = 'user2')

        self.testPost = Post.objects.create(category_id = 1, title = 'testpost', 
            author_id = 1, content = 'testing post', excerpt = 'testing post', 
            slug = 'testing-post', post_status = 'published')

        client.login(username = self.user1.username, password = 'user1')  

        url = reverse(('blog_api:retrievedestroyupdate'), kwargs={'pk': 1})      

        data = { 
            'title' : 'testpost1', 
            'author' : 1,
            'content' : 'testing post1', 
            'excerpt' : 'testing post1', 
            'slug' : 'testing-post1',
            'post_status' : 'published',
            }

        
        response = client.put(url, data, format = 'json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

