"""
WSGI config for mainproj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
# import sys

from django.core.wsgi import get_wsgi_application
#
# # Set environment variables for django to use
os.environ['DJANGO_SETTINGS_MODULE'] = 'mainproj.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainproj.settings")

# sys.path.append('/home/califuse/public_html/califuse/mainproj')
# sys.path.append('/home/califuse/public_html/califuse')
application = get_wsgi_application()
