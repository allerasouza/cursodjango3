from django.contrib import admin
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin): # Create customization class for Post
    list_display = [
        'title', 'sub_title', 'full_name',
        'categories', 'deleted'
    ]
    search_fields = ['title', 'sub_title']
    # fields = ('title', 'sub_title', 'content')

    # def get_queryset(self, request):
    #     return Post.objects.filter(deleted=False)

class ContactAdmin(admin.ModelAdmin): # Create customization class for Post
    list_display = [
        'name'
    ]
    search_fields = ['name']

# Register your models here.
admin.site.register(Post, PostAdmin) # Apply customization to Post
admin.site.register(Contact, ContactAdmin) # Apply customization to Post
