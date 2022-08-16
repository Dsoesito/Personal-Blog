from django.shortcuts import get_object_or_404, render

from op_blog.models import Post, Comment
from op_blog.forms import CommentForm

# Create your views here.

def all_portfolio_posts(request):
    all_portfolio_posts = Post.objects.filter(topic__iexact="Programming").order_by("-date")
    return render(request, "portfolio/index.html",{
        "posts" : all_portfolio_posts
    })

def single_portfolio_post(request, slug):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        user_email = request.POST["user_email"]
        text = request.POST["text"]
        post = Post.objects.get(slug=slug)

        comment = Comment(user_name=user_name, user_email=user_email, text=text, post=post)
        comment.save()

    single_portfolio_post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm()
    post = Post.objects.get(slug=slug)
    all_portfolio_comments = post.comments.all().order_by("-id")

    comments_empty = False
    if len(all_portfolio_comments) == 0:
        comments_empty = True

    return render(request, "portfolio/single-portfolio-post.html", {
        "portfolio_post": single_portfolio_post,
        "form": comment_form,
        "comments": all_portfolio_comments,
        "comments_empty": comments_empty
    })


