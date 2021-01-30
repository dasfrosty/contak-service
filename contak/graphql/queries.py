import time
from typing import Optional, List

import graphene as g
from graphql.execution.base import ResolveInfo

from contak import models
from contak.graphql.object_types import User, Contact

LOAD_DELAY = 0.5


class Query(g.ObjectType):

    current_user = g.Field(User)

    contact = g.Field(Contact, id=g.ID(required=True))
    all_contacts = g.NonNull(g.List(g.NonNull(Contact)))

    @staticmethod
    def resolve_current_user(_parent: None, info: ResolveInfo) -> Optional[User]:
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        return user

    @staticmethod
    def resolve_contact(
        _parent: None, _info: ResolveInfo, id: str
    ) -> Optional[models.Contact]:
        time.sleep(LOAD_DELAY)
        try:
            return models.Contact.objects.get(id=id)
        except models.Contact.DoesNotExist:
            return None

    @staticmethod
    def resolve_all_contacts(_parent: None, _info: ResolveInfo) -> List[models.Contact]:
        time.sleep(LOAD_DELAY)
        return models.Contact.objects.all()
