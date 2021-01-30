import time
from typing import Optional, List

import graphene as g
from graphql.execution.base import ResolveInfo

from contak import models
from contak.graphql.object_types import Contact

LOAD_DELAY = 0.5


class Query(g.ObjectType):

    contact = g.Field(Contact, id=g.ID(required=True))
    all_contacts = g.NonNull(g.List(g.NonNull(Contact)))

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
