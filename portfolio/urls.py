from django.urls import path

from . import views

urlpatterns = [
    path("", views.all_portfolio_posts, name="portfolio-page"),
    path("<slug:slug>", views.single_portfolio_post, name="single-portfolio-post")
]
