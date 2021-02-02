import factory

from django.contrib.auth import get_user_model
from contak.models import Contact


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f"username_{n}")
    password = "password"


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    note = factory.Faker("sentence")

    user = factory.SubFactory(UserFactory)
