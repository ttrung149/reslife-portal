from django.contrib import admin
from .models import IR
# Register your models here.


class IRAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('title', 'date_posted', 'author')


admin.site.register(IR, IRAdmin)
