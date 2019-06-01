from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User
from residencies.models import Building, Resident
# Create your models here.


class IR(models.Model):
    title = models.CharField(max_length=100)

    student_ID = models.CharField(max_length=10)

    location = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    date_of_incident = models.DateTimeField(default=timezone.now)

    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ir-detail', kwargs={'pk': self.pk})
