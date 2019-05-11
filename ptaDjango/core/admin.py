from django.contrib import admin
from .models import Post
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

admin.site.register(Post, PostsAdmin)