import time

import graphene as g
from graphql.execution.base import ResolveInfo
from graphql_jwt.decorators import login_required

from contak import models
from .object_types import Contact

LOAD_DELAY = 0.5


class CreateContactInput(g.InputObjectType):
    first_name = g.String(required=True)
    last_name = g.String(required=True)
    note = g.String(required=True)


class CreateContactMutation(g.Mutation):
    class Arguments:
        input = g.NonNull(CreateContactInput)

    contact = g.Field(Contact, required=True)

    @staticmethod
    @login_required
    def mutate(_parent: None, info: ResolveInfo, input: CreateContactInput):
        time.sleep(LOAD_DELAY)

        user = info.context.user
        contact: models.Contact = models.Contact.objects.create(
            first_name=input.first_name,
            last_name=input.last_name,
            note=input.note,
            user=user,
        )
        contact.full_clean()

        return CreateContactMutation(contact=contact)


class UpdateContactInput(g.InputObjectType):
    contact_id = g.ID(required=True)
    first_name = g.String(required=True)
    last_name = g.String(required=True)
    note = g.String(required=True)


class UpdateContactMutation(g.Mutation):
    class Arguments:
        input = g.NonNull(UpdateContactInput)

    contact = g.Field(Contact, required=True)

    @staticmethod
    @login_required
    def mutate(_parent: None, info: ResolveInfo, input: UpdateContactInput):
        time.sleep(LOAD_DELAY)

        user = info.context.user
        contact: models.Contact = models.Contact.objects.get(
            id=input.contact_id, user=user
        )
        contact.first_name = input.first_name
        contact.last_name = input.last_name
        contact.note = input.note
        contact.full_clean()
        contact.save()

        return UpdateContactMutation(contact=contact)


class Mutation:
    create_contact = CreateContactMutation.Field()
    update_contact = UpdateContactMutation.Field()
