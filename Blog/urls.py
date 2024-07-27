from django.urls import path
from .views import BlogDetailView, BlogListView

urlpatterns = [
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("", BlogListView.as_view(), name="home"),
]
