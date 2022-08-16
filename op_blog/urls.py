from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_op_posts, name="op-page"),
    path("<slug:slug>", views.single_op_post, name="single-op-post")
    ]