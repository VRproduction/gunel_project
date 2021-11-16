from django.urls import path

from . import views

app_name = 'blog_app'

urlpatterns = [
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name="blog-detail")
]