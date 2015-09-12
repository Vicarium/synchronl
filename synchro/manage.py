#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    try:
        test = os.environ['IS_PRODUCTION']
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "synchro.settings.production")
    except:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "synchro.settings")

   # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "synchro.settings.production")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
