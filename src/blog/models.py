from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Post(models.Model):

    # model manager helps to query our posts in first place. (it drops the use of posts.objects.all 
    # and forces to use postobject.objects.all)

    class PostObjects(models.Manager):      
        def get_queryset(self):             # this only returns the posts which have status of 'published'
            return super().get_queryset().filter(post_status = 'published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250, blank=False)
    excerpt = models.TextField()
    content = models.TextField(blank=False)
    slug = models.SlugField(max_length=250, unique_for_date='publish_date')    # for url
    publish_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    post_status = models.CharField(max_length=10, choices=options, default='published')

    objects = models.Manager()      # default manager
    postobjects = PostObjects()     # custom manager


    class Meta:                     # return the data in descending order of publish date by default
        ordering = ('-publish_date',)

    def __str__(self):              # used to view the string representation of query set
        return self.title 



