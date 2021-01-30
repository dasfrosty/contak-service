from graphene_django import DjangoObjectType

from contak import models


class Contact(DjangoObjectType):
    class Meta:
        model = models.Contact
        fields = ["id", "first_name", "last_name", "created", "modified"]
