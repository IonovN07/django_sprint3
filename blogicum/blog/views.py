from django.http import Http404
from django.shortcuts import render



def index(request):
    return render(request, 'blog/index.html' )
#{'posts': posts}

def post_detail(request, post_id):
    #if post_id not in posts_id:
        #raise Http404(f'Запрашиваемая вами страница {post_id} не найдена')
    return render(request, 'blog/detail.html')
#{'post': posts_id[post_id]}

def category_posts(request, category_slug):
    return render(request, 'blog/category.html')

#{'category': category_slug}