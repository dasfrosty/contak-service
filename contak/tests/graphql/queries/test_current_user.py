from contak.tests.factories import UserFactory
from contak.tests.graphql.graphql_test_case import GraphqlTestCase


class TestCurrentUserQuery(GraphqlTestCase):
    def test_current_user_is_none(self):
        query = """
            query currentUser {
                currentUser {
                    id
                    username
                    email
                }
            }
        """
        expected_data = {"currentUser": None}

        result = self.client.execute(query)
        self.assertResultHasNoErrors(result)

        self.assertEqual(result.data, expected_data)

    def test_current_user_is_not_none(self):
        user = UserFactory()
        self.client.authenticate(user)

        query = """
            query currentUser {
                currentUser {
                    id
                    username
                    email
                }
            }
        """

        expected_data = {
            "currentUser": {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
            }
        }

        result = self.client.execute(query)
        self.assertResultHasNoErrors(result)
        self.assertEqual(result.data, expected_data)
