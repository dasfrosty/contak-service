from typing import Optional

import graphene as g
from graphql.execution.base import ResolveInfo

from contak.graphql.object_types import User


class Query:

    current_user = g.Field(User)

    @staticmethod
    def resolve_current_user(_parent: None, info: ResolveInfo) -> Optional[User]:
        user = info.context.user
        return user if user.is_authenticated else None
