from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

import datetime

from django.contrib.auth import get_user_model
from django.conf import settings
# User = settings.AUTH_USER_MODEL
User = get_user_model()


# def get_agent():
#     return User.objects.added_by(username)


class Tour(models.Model):
    tour_name = models.CharField(max_length=200)
    agent = models.ForeignKey(
        User, to_field="username", on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    duration = models.IntegerField()
    price = models.IntegerField()
    body = models.TextField()

    def __str__(self):
        return self.tour_name

    def __str__(self):
        return self.city_name

    def get_absolute_url(self):
        return reverse("tour_detail", kwargs={"pk": self.pk})
