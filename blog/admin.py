from django.contrib import admin
from .models import Post

admin.site.site_title = 'Admin'
admin.site.site_header = 'CodeBlog Administration'
admin.site.index_title = 'CodeBlog' 

admin.site.register(Post)