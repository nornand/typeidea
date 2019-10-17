'''blog应用的view'''
from django.shortcuts import render

from .models import Post

def post_list(request, category_id=None, tag_id=None):
    '''文章列表'''
    tag = None
    category = None
    item_list = []

    if tag_id:
        item_list, tag = Post.get_by_tag(tag_id=tag_id)
    elif category_id:
        item_list, category = Post.get_by_category(category_id=category_id)
    else:
        item_list = Post.objects.all()

    context = {
        'post_list': item_list,
        'tag': tag,
        'category': category
    }

    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    '''文章详情'''
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    return render(request, 'blog/detail.html', context={'post': post})
