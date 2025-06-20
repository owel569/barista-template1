"""
ASGI config for barista_cafe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "barista_cafe.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barista_cafe.settings')
>>>>>>> ffce6af89a3517af95eb5d7be291ed190449e930

application = get_asgi_application()
