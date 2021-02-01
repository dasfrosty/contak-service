from graphene import ObjectType, Schema

from contak.auth.mutations import Mutation as AuthMutation
from contak.auth.queries import Query as AuthQuery
from contak.graphql.mutations import Mutation as ContakMutation
from contak.graphql.queries import Query as ContakQuery


class Query(AuthQuery, ContakQuery, ObjectType):
    pass


class Mutation(AuthMutation, ContakMutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
