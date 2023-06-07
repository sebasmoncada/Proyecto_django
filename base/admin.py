from django.contrib import admin
from .models import Post, Comment, Soport, Like, Payment


# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Soport)
admin.site.register(Like)
admin.site.register(Payment)
