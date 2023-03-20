from django.contrib import admin
from .models import Post
from .models import PostFootballer

admin.site.register(Post)

admin.site.register(PostFootballer)

# Register your models here.
