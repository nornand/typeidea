'''blog应用的view'''
from django.shortcuts import render

from .models import Post, Tag

def post_list(request, category_id=None, tag_id=None):
    '''文章列表'''
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            item_list = []
        else:
            item_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        item_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            item_list = item_list.filter(category_id=category_id)

    return render(request, 'blog/list.html', context={'post_list': item_list})


def post_detail(request, post_id=None):
    '''文章详情'''
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    return render(request, 'blog/detail.html', context={'post': post})
