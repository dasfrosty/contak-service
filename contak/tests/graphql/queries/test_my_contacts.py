from contak.models import Contact
from contak.tests.factories import UserFactory, ContactFactory
from contak.tests.graphql.graphql_test_case import GraphqlTestCase

MY_CONTACTS_QUERY = """
    query myContacts {
        myContacts {
            id
            firstName
            lastName
            note
            user {
                username
            }
        }
    }
"""


def to_graphql_contact(contact: Contact):
    return {
        "id": str(contact.id),
        "firstName": contact.first_name,
        "lastName": contact.last_name,
        "note": contact.note,
        "user": {"username": contact.user.username},
    }


class TestMyContactsQuery(GraphqlTestCase):
    def test_login_required(self):
        result = self.client.execute(MY_CONTACTS_QUERY)
        self.assertResultHasLoginRequiredError(result)

    def test_no_contacts(self):
        user = UserFactory()
        self.client.authenticate(user)

        expected_data = {"myContacts": []}

        result = self.client.execute(MY_CONTACTS_QUERY)
        self.assertResultHasNoErrors(result)
        self.assertEqual(result.data, expected_data)

    def test_only_my_contacts(self):
        user, other_user = UserFactory.create_batch(2)
        self.client.authenticate(user)

        my_contacts = sorted(
            ContactFactory.create_batch(3, user=user),
            key=lambda contact: (contact.last_name, contact.first_name, contact.id),
        )
        ContactFactory.create_batch(2, user=other_user)

        expected_data = {
            "myContacts": [to_graphql_contact(contact) for contact in my_contacts]
        }

        result = self.client.execute(MY_CONTACTS_QUERY)
        self.assertResultHasNoErrors(result)
        self.assertEqual(result.data, expected_data)
