from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin): # Create customization class for Post
    list_display = ['title', 'sub_title', 'full_name', 'categories']
    search_fields = ['title', 'sub_title']
    # fields = ('title', 'sub_title', 'content')

# Register your models here.
admin.site.register(Post, PostAdmin) # Apply customization to Post
