import graphene as g

from contak.graphql.queries import Query


schema = g.Schema(query=Query)
