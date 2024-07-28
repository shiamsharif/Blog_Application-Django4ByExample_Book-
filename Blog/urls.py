from django.urls import path
from .views import BlogDetailView, BlogListView, UserPostListView

urlpatterns = [
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path('<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path("", BlogListView.as_view(), name="home"),
]
