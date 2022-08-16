from django.shortcuts import get_object_or_404, render

from op_blog.models import Post, Comment
from .forms import CommentForm

# Create your views here.

def all_op_posts(request):
    all_op_posts = Post.objects.filter(topic__iexact="One Piece").order_by("-date")
    return render(request, "op_blog/index.html",{
        "posts": all_op_posts
    })

def single_op_post(request, slug):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        user_email = request.POST["user_email"]
        text = request.POST["text"]
        post = Post.objects.get(slug=slug)

        comment = Comment(user_name=user_name, user_email=user_email, text=text, post=post)
        comment.save()
        
    single_op_post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm()
    post = Post.objects.get(slug=slug)
    all_op_comments = post.comments.all().order_by("-id")

    comments_empty = False
    if len(all_op_comments) == 0:
        comments_empty = True

    return render(request, "op_blog/single-op-post.html", {
        "op_post": single_op_post,
        "form": comment_form,
        "comments": all_op_comments,
        "comments_empty": comments_empty
    })
    