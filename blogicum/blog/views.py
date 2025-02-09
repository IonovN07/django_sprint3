from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post


def filter_published(posts = Post.objects.all()):
    return posts.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=timezone.now())


def index(request):
    return render(
        request,
        'blog/index.html',
        {'posts': filter_published()[:5]})


def post_detail(request, post_id):
    return render(
        request,
        'blog/detail.html',
        {'post': get_object_or_404(filter_published(), id=post_id)})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    return render(
        request,
        'blog/category.html',
        {'category': category,
            'posts': filter_published(category.posts)})
