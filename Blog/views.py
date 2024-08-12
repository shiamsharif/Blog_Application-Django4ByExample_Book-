from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from django.views.decorators.http import require_POST

# Create your views here.
class BlogListView(ListView):
    
    queryset = Post.published.all()
    template_name = "../templates/blog/post/home.html"
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context["posts"] = posts
        
        # Create a dictionary to store comments for each post
        post_comments = {}
        
        for post in posts:
            # Filter comments related to the current post
            comments = Comment.objects.filter(post=post)
            post_comments[post] = comments
        
        context["post_comments"] = post_comments
        return context


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/post/comment.html',
                  {'post': post,
                   'form': form,
                   'comment': comment})


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
    
