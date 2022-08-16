from django.shortcuts import get_object_or_404, render

from op_blog.models import Post, Comment
from op_blog.forms import CommentForm

# Create your views here.

def tech_page(request):
    all_tech_posts = Post.objects.filter(topic__iexact="Tech").order_by("-date")
    return render(request, "tech_blog/index.html",{
        "posts": all_tech_posts
    })

def single_tech_post(request, slug):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        user_email = request.POST["user_email"]
        text = request.POST["text"]
        post = Post.objects.get(slug=slug)

        comment = Comment(user_name=user_name, user_email=user_email, text=text, post=post)
        comment.save()

    single_tech_post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm()
    post = Post.objects.get(slug=slug)
    all_tech_comments = post.comments.all().order_by("-id")

    comments_empty = False
    if len(all_tech_comments) == 0:
        comments_empty = True

    return render (request, "tech_blog/single-tech-post.html", {
        "tech_post": single_tech_post,
        "form": comment_form,
        "comments": all_tech_comments,
        "comments_empty": comments_empty
    })
