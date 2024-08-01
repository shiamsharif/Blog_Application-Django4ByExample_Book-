from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "../templates/blog/post/home.html"
    context_object_name = 'posts'
    paginate_by = 2


class BlogDetailView(DetailView):
    model = Post
    template_name="../templates/blog/post/detail.html"

class UserPostListView(ListView):
    model = Post
    template_name = '../templates/blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return Post.objects.filter(author=user)
    
