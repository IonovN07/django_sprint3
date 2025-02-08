from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post


def filter_data(queryset):
    return queryset.select_related(
        'category', 'location', 'author'
        ).filter(is_published=True, pub_date__lt=timezone.now())


def index(request):
    return render(
        request, 
        'blog/index.html', 
        {'post_list': filter_data(Post.objects.filter(
            category__is_published=True))[:5]})


def post_detail(request, post_id):
    return render(
        request, 
        'blog/detail.html', 
        {'post': get_object_or_404(filter_data(Post.objects.filter(
            category__is_published=True)), id=post_id)})


def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.filter(is_published=True), 
               slug=category_slug)
    return render(
        request, 
        'blog/category.html', {
            'category': category, 
            'post_list': filter_data(category.posts_in_category)})