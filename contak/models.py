from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Contact(TimeStampedModel):
    first_name = models.TextField()
    last_name = models.TextField()
    note = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["last_name", "first_name", "id"]

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"
