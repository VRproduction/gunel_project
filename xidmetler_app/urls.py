from django.urls import path
from . import views

app_name = 'xidmetler_app'

urlpatterns = [
    path('xidmetlerimiz/<slug:slug>/', views.NewsDetailView.as_view(), name='news-detail')
]