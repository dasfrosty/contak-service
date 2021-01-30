#!/usr/bin/env python
import os
import sys

from dotenv import find_dotenv, load_dotenv

if dotenv := find_dotenv():
    load_dotenv(dotenv)


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "BaseSettings")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
