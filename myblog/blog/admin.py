from django.contrib import admin
from .models import Post, Coments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor')


@admin.register(Coments)
class Coments(admin.ModelAdmin):
    list_display = ('name', 'post')