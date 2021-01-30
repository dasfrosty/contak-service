# contak-service

Demo Django service for managing contacts.

## Getting Started

### Prerequisites

1. Postgres version 12 or later.


### Setup

1. Clone this repo and then open a terminal window and `cd` to the project root directory.


1. Install python dependencies:

   ```
   poetry install
   ```

1. Create a `.env` file from the [.env-sample](.env-sample) provided in the repo and fill
in the appropriate values.

   ```
   cp .env-sample .env
   ```

1. Create a postgres database for the project:

   ```
   createdb contak
   ```

### Run the Tests and Checks

1. Run the tests:
   ```
   poetry run pytest .
   ```

1. Run linting and formatting checks:
   ```
   poetry run flake8 .
   poetry run black --check .
   ```

1. Run type checking:
   ```
   poetry run mypy .
   ```

### Run the Services Locally

1. Run the Django database migration(s)

   ```
   poetry run ./manage.py migrate
   ```

1. Run the Django Service

   ```
   poetry run ./manage.py runserver
   ```

## Development

### GraphQL Schema

1. Update the graphql_schema.json file:

   ```
   poetry run ./manage.py graphql_schema
   git add schema.json
   ```
