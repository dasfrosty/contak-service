import time
from typing import Optional, List

import graphene as g
from graphql.execution.base import ResolveInfo
from graphql_jwt.decorators import login_required, superuser_required
from contak import models
from contak.graphql.object_types import Contact

LOAD_DELAY = 0.5


class Query:
    contact = g.Field(Contact, id=g.ID(required=True))
    all_contacts = g.NonNull(g.List(g.NonNull(Contact)))

    my_contacts = g.NonNull(g.List(g.NonNull(Contact)))

    @staticmethod
    @login_required
    def resolve_contact(
        _parent: None, info: ResolveInfo, id: str
    ) -> Optional[models.Contact]:
        time.sleep(LOAD_DELAY)
        user = info.context.user
        try:
            return models.Contact.objects.get(id=id, user=user)
        except models.Contact.DoesNotExist:
            return None

    @staticmethod
    @superuser_required
    def resolve_all_contacts(_parent: None, _info: ResolveInfo) -> List[models.Contact]:
        time.sleep(LOAD_DELAY)
        return models.Contact.objects.all()

    @staticmethod
    @login_required
    def resolve_my_contacts(_parent: None, info: ResolveInfo) -> List[models.Contact]:
        time.sleep(LOAD_DELAY)
        user = info.context.user
        return models.Contact.objects.filter(user=user)
