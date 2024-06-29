from django.contrib import admin
from .models import Post, Category, Comments

admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(Category)
