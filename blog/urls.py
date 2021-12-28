from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    # ex: /
    path('', views.posts_view, name='posts'),
    # ex: /post/23
    path('post/<int:post_id>', views.post_view, name='post'),
    # ex: /search/
    path('search/', views.search_view, name='search'),
    # ex: /category/programming
    path('category/<int:category_id>', views.category_view, name="category"),
]
