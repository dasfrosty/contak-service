from django.contrib.auth import models as auth_models
from graphene_django import DjangoObjectType

from contak import models


class User(DjangoObjectType):
    class Meta:
        model = auth_models.User
        fields = ["id", "username", "email"]


class Contact(DjangoObjectType):
    class Meta:
        model = models.Contact
        fields = ["id", "first_name", "last_name", "created", "modified"]
