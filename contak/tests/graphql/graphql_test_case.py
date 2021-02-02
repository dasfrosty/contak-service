from graphql.execution.base import ExecutionResult
from graphql_jwt.testcases import JSONWebTokenTestCase


class GraphqlTestCase(JSONWebTokenTestCase):
    maxDiff = 9999

    def assertResultHasNoErrors(self, result: ExecutionResult):
        self.assertIsNone(result.errors)
        self.assertFalse(result.invalid, msg="Result is invalid!")
        self.assertIsNotNone(result.data, msg="No data in result!")

    def assertResultHasErrors(self, result: ExecutionResult, errors=None):
        self.assertIsNotNone(result.errors)
        self.assertGreater(len(result.errors), 0)

        if errors is not None:
            error_messages = [error.message for error in result.errors]
            self.assertCountEqual(error_messages, errors)

    def assertResultHasLoginRequiredError(self, result: ExecutionResult):
        self.assertResultHasErrors(
            result, ["You do not have permission to perform this action"]
        )
