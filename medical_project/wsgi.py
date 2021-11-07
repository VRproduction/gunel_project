"""
WSGI config for medical_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
# from whitenoise import WhiteNoise	
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_project.settings')

application = get_wsgi_application()
# application = WhiteNoise(application, root='/var/www/html/static/')
# application.add_files('/var/www/html/static', prefix='more-files/')
