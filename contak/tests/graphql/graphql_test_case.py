from graphql_jwt.testcases import JSONWebTokenTestCase
from graphql.execution.base import ExecutionResult


class GraphqlTestCase(JSONWebTokenTestCase):
    def assertResultHasNoErrors(self, result: ExecutionResult):
        self.assertIsNone(result.errors)
        self.assertFalse(result.invalid, msg="Result is invalid!")
        self.assertIsNotNone(result.data, msg="No data in result!")
