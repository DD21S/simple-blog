from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Category, Comment

# Create your views here.

def posts_view(request):
    posts = Post.objects.all().order_by('-id')

    context = {
        "posts": posts,
        "header": True,
    }

    return render(request, 'blog/posts.html', context)

def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if 'comment' in request.POST:
        comment = Comment(text_comment=request.POST["comment"], post=post)
        comment.save()

    context = {
        "post": post,
        "header": False,
    }

    return render(request, 'blog/post.html', context)

def search_view(request):
    if 'search' in request.POST:
        search = request.POST['search']
        results = Post.objects.filter(
            text_post__icontains=search
        ).order_by('-id')

        context = {
            "posts": results,
            "search": search,
            "header": False,
        }

        return render(request, 'blog/search.html', context)

    return HttpResponseRedirect(reverse('blog:posts'))

def category_view(request, category_id):
    results = get_object_or_404(Category, pk=category_id)

    context = {
        "posts": results.post_set.all,
        "category": results.name,
        "header": False
    }

    return render(request, 'blog/category.html', context)
