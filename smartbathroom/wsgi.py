"""
WSGI config for smartbathroom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from smartb import mqtt_thread

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smartbathroom.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

mqtt_thread.start_mqtt_listener()