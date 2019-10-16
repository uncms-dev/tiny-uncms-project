#!/usr/bin/env python -Wa
import os
import pwd
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tiny_project.settings.local")
    os.environ.setdefault("DB_USER", pwd.getpwuid(os.getuid()).pw_name)
    os.environ.setdefault("DB_NAME", "tiny_project")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
