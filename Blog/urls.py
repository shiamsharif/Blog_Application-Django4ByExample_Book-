from django.urls import path
from .views import BlogDetailView, BlogListView, UserPostListView, post_comment
from . import views


urlpatterns = [
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path('<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path("", BlogListView.as_view(), name="home"),
]
