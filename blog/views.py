from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Category, Tag, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.utils import timezone

def blog_index_view(request, cat=None, tag=None, author=None):
    posts = Post.objects.filter(post_status=True, published_date__lte= timezone.now())
    if cat:
        posts = posts.filter(categories__name=cat)
    if tag:
        posts = posts.filter(tags__name=tag)
    if author:
        posts = posts.filter(author__username=author)

    p = Paginator(posts, 8)
    if request.method == 'GET':
        try:
            page_number = request.GET.get('page')
            if page_number:
                if int(page_number) > p.num_pages:
                    return redirect(f'/blog/?page={p.num_pages}')
                elif int(page_number) < 1:
                    return redirect('/blog/')
                else:
                    posts = p.page(page_number)
            else:
                posts = p.page(1)

        except PageNotAnInteger:
            # posts = p.page(1).object_list
            # return redirect('/blog/')
            posts = p.get_page(1)
        except EmptyPage:
            # posts = p.page(1).object_list
            # return redirect('/blog/')
            posts = p.get_page(1)
            return redirect('/blog/')
        except ValueError:
            posts = p.get_page(1)
            return redirect('/blog/')

    context = {'posts':posts}
    return render(request, 'blog/blog.html', context)

def blog_single_view(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data.get('name')    
            # email = form.cleaned_data.get('email')    
            # text = form.cleaned_data.get('text')   
            form.save() 
            msg = """Your comment has been successfully received.
            After site admins have approved your comment, it will shown
            on the website."""
            messages.add_message(request, messages.SUCCESS, msg)
        else:
            msg= """Something went wrong! try sending your comment again later."""
            messages.add_message(request, messages.ERROR, msg)

    post = get_object_or_404(Post, id=pid, post_status=True, published_date__lte=timezone.now())
    add_view(pid, post.counted_views)
    post = get_object_or_404(Post, id=pid, post_status=True, published_date__lte=timezone.now())
    
    posts_list = list(Post.objects.filter(post_status=True, published_date__lte= timezone.now()).values('id'))
    posts_list = sorted(posts_list, key=lambda x: x['id'])
    
    query_number = 0
    for dict in posts_list:
        if dict['id'] == pid:
            break
        else:
            query_number += 1

    next_query_number = query_number + 1
    prev_query_number = query_number - 1
    max_id = posts_list[-1]['id']

    if pid == 1:
        next_post_id = posts_list[next_query_number]['id']
        prev_post_id = None
    elif pid == max_id:
        next_post_id = None
        prev_post_id = posts_list[prev_query_number]['id']
    else:
        next_post_id = posts_list[next_query_number]['id']
        prev_post_id = posts_list[prev_query_number]['id']

    cats = Category.objects.filter(post= pid)
    tags = Tag.objects.filter(post= pid)

    comments = Comment.objects.filter(post= pid, is_approved=True)

    form = CommentForm()
    context = {'post': post, 'cats':cats, 'tags':tags, 'form':form, 'comments':comments,
               'next_post_id':next_post_id, 'prev_post_id':prev_post_id}
    return render(request, 'blog/blog-single.html', context)

def blog_search_view(request):
    posts = Post.objects.filter(post_status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains= s) | posts.filter(title__contains= s)
            
    context= {'posts': posts}
    return render(request, 'blog/blog.html', context)

def add_view(pid, counted_views):
    views = counted_views + 1
    post = Post.objects.filter(id= pid).update(counted_views= views)