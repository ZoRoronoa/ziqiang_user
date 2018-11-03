# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse


def output(request):
    from blog.models import Blog
    title = Blog.title
    content = Blog.content
    blogs = Blog.objects.all()
    return render(request, 'output.html', locals())


def search(request):
    from blog.models import Blog

    q = request.GET.get('q')

    #q = q.encode("utf-8")
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'errors.html', {'error_msg': error_msg})

    else:
        post_list = Blog.objects.filter(content__icontains=q)
        return render(request, 'results.html', {'error_msg': error_msg, 'post_list': post_list})



