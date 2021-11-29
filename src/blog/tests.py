from django.contrib import auth
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

# testing creates posts on dummy database


# TESTING BLOG MODELS
class TestCreatPost(TestCase):

    #  method for creating data in database
    @classmethod
    def setUpTestData(self):
        testCategory = Category.objects.create(name = 'django')
        testUser = User.objects.create_user(username = 'testUser', password = '1234')
        testPost = Post.objects.create(category_id = 1, title = 'testpost', 
            author_id = 1, content = 'testing post', excerpt = 'testing post', 
            slug = 'testing-post', post_status = 'published')


    # test for checking retrieved data from database
    def testPostContent(self):        
        post = Post.objects.get(id = 1)
        cat = Category.objects.get(id = 1)

        author = f'{post.author}'
        content = f'{post.content}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        st = f'{post.post_status}'

        self.assertEqual(author, 'testUser')
        self.assertEqual(content, 'testing post')
        self.assertEqual(title, 'testpost')
        self.assertEqual(excerpt, 'testing post')
        self.assertEqual(st, 'published')

        self.assertEqual(str(post), 'testpost')
        self.assertEqual(str(cat), 'django')
