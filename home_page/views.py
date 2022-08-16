from django.shortcuts import render

from op_blog.models import Post

# Create your views here.

def home_page(request):
    latest_op_post = Post.objects.filter(topic__iexact="One Piece").order_by("-date")[:1]
    latest_tech_post = Post.objects.filter(topic__iexact="Tech").order_by("-date")[:1]
    latest_programming_post = Post.objects.filter(topic__iexact="Programming").order_by("-date")[:1]
    return render(request, "home_page/index.html",{
        "op_post": latest_op_post,
        "tech_post": latest_tech_post,
        "programming_post": latest_programming_post
    })

def about_me(request):
    return render(request, "home_page/about.html")
    