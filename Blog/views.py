from django.views.generic import ListView, DeleteView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "../templates/blog/post/home.html"
    context_object_name = 'posts'
    paginate_by = 2


class BlogDetailView(DeleteView):
    model = Post
    template_name="../templates/blog/post/detail.html"
