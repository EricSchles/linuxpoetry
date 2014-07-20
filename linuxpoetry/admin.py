"""Enable automatic admin pages for linuxpoetry."""

from django.contrib import admin

from linuxpoetry.models import Post, PostTag, BlogPost, BlogPostTag

admin.site.register(Post)
admin.site.register(PostTag)
admin.site.register(BlogPost)
admin.site.register(BlogPostTag)
