import graphene as g
import graphql_jwt
from contak.graphql.queries import Query


class Mutation(g.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = g.Schema(query=Query, mutation=Mutation)
