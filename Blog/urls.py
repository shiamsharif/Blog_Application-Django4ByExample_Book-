from django.urls import path
from .views import BlogDetailView, BlogListView, UserPostListView, post_comment


urlpatterns = [
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path('<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('<int:post_id>/comment/', post_comment.as_view(), name='post_comment'),
    path("", BlogListView.as_view(), name="home"),
]
