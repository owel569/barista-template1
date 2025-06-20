"""
WSGI config for barista_cafe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barista_cafe.settings')

application = get_wsgi_application()
<<<<<<< HEAD

=======
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930
