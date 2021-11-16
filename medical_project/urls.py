"""medical_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from qebul_app.views import appoinment
from medical_app.views import homepage
from contact_app.views import contact
from xidmetler_app.views import bizim_xidmetler
from medi_app.views import med
from blog_app.views import blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('',include('blog_app.urls', namespace='blog_app')),
    path('',include('xidmetler_app.urls', namespace='xidmetler_app')),
    path('qəbulayazıl/', appoinment, name="appoinment"),
    path('əlaqə/', contact, name="contact"),
    path('xidmətlərimiz/', bizim_xidmetler, name="xidmetler"),
   # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', blog, name="blog"),
    path('medi/', med , name="media"), 
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
	static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
