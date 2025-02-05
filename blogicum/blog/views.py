from django.http import Http404
from blog.models import Category, Location, Post
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.utils import timezone


def index(request):
    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True, 
        pub_date__lt=timezone.now(), 
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    # post = get_object_or_404(
    #     Post.objects.select_related(
    #         'category', 'location', 'author'
    #         ).filter(is_published=True, 
    #     pub_date__lt=timezone.now(), 
    #     category__is_published=True), id=post_id)
    try:
        post = Post.objects.select_related(
            'category', 'location', 'author'
        ).filter(is_published=True, 
                pub_date__lt=timezone.now(), 
                category__is_published=True
        ).get(id=post_id)
    except Post.DoesNotExist:
        raise Http404(f'Запрашиваемая вами страница {post_id} не найдена')
    return render(request, 'blog/detail.html', {'post': post})
    
#{'post': posts_id[post_id]}

def category_posts(request, category_slug):
    
    category = get_object_or_404(
        Category.objects.filter(is_published=True,
            slug=category_slug))
    
    posts = category.posts_in_category.select_related(
        'category', 'location', 'author'
    ).filter(is_published=True, pub_date__lt=timezone.now())
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, 'blog/category.html', context)

#{'category': category_slug}