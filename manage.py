#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "barista_cafe.settings")
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barista_cafe.settings')
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930
    main()
