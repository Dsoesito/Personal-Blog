from django.urls import path
from . import views

urlpatterns = [
    path("", views.tech_page, name="tech-page"),
    path("<slug:slug>", views.single_tech_post, name="single-tech-post")
    ]
    