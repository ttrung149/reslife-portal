from django.db import models
from django.contrib.auth.models import User
from staffs.models import Staff

# Create your models here.


class Building(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.CharField(max_length=15)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    pass_inspection = models.BooleanField(default=False)
    inspected_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='inspected_by', blank=True, null=True)

    inspection_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.building.name + ' ' + self.room_number


class Resident(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_ID = models.CharField(max_length=10)
    student_email = models.EmailField()

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    is_checked_out = models.BooleanField(default=False)
    checked_out_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='checked_out_by', blank=True, null=True)

    checked_out_time = models.DateTimeField(null=True, blank=True)

    under_RA = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='under_RA')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
