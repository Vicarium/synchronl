#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    if os.environ['IS_PRODUCTION']:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "synchro.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "synchro.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
