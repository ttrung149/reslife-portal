from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.site_header = 'ResLife Portal Admin'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('title', 'date_posted', 'author')


admin.site.register(Post, PostAdmin)
