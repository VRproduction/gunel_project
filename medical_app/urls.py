from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from medical_app.views import homepage, appoinment
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('appoinment/', appoinment, name="appoinment")
] 
