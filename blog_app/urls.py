from django.urls import path

from . import views

app_name = 'blog_app'

urlpatterns = [
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name="blog-detail")
]