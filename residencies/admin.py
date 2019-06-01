from django.contrib import admin

# Register your models here.
from residencies.models import Building
from residencies.models import Room
from residencies.models import Resident


class BuildingAdmin(admin.ModelAdmin):
    search_fields = ['name']


class RoomAdmin(admin.ModelAdmin):
    list_display = ('building', 'room_number')
    list_filter = ('building', 'room_number')


class ResidentAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
    list_display = ('first_name', 'last_name', 'room', 'under_RA')
    list_filter = ('first_name', 'last_name', 'room', 'under_RA')


admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Resident, ResidentAdmin)
