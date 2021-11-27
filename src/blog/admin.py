from django.contrib import admin
from .models import Category, Post

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',),}
admin.site.register(Category)

