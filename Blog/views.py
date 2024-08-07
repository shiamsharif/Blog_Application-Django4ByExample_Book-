from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import EmailPostForm

# Create your views here.
class BlogListView(ListView):
    
    queryset = Post.published.all()
    template_name = "../templates/blog/post/home.html"
    context_object_name = 'posts'
    paginate_by = 2
    
# def post_share(request, post_id):
#     post = get_object_or_404(Post, id=post_id, ststus=Post.Status.PUBLISHED)
#     if request.method == 'POST':
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#     else:
#         form = EmailPostForm()
#     request render


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
    
