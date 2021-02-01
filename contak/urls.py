from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from rest_framework.routers import DefaultRouter

from .views import ContactViewSet

GRAPHQL_URL = "/contak/graphql"

router = DefaultRouter()
router.register(r"contact", ContactViewSet)

urlpatterns = [
    # GraphQL routes
    path("", RedirectView.as_view(url=GRAPHQL_URL)),
    path("graphql", csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True)))),
    # REST routes
    path("api/", include(router.urls)),
    # login URLs for the browsable API
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
