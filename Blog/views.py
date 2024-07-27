from django.views.generic import ListView, DeleteView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "../templates/blog/post/home.html"
    context_object_name = 'posts'


class BlogDetailView(DeleteView):
    model = Post
    template_name="../templates/blog/post/detail.html"
