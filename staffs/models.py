from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        'residencies.Room', on_delete=models.CASCADE)

    is_GRD = models.BooleanField(default=False)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + ' ' + self.user.last_name
        return self.user.username

    def save(self):
        super().save()
