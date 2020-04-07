from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Blog, Event, Comment

def index(request):
    
    events = get_list_or_404(Event)
    blogs = get_list_or_404(Blog)[:3]
    return render(request, 'mainapp/index.html', {
        'events': events,
        'blogs': blogs,
    })

def about(request):
    return render(request, 'mainapp/about.html')

def comment(request, blog_id):
    name = request.POST['name']
    content = request.POST['comment']
    blog = Blog.objects.get(pk=int(blog_id))
    comment = Comment.objects.create(blog=blog, author=name, content=content)
    return HttpResponseRedirect(reverse('mainapp:blog_detail', args=(blog_id,)))
    

def listBlogContent(request):
    blogs = get_list_or_404(Blog)
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mainapp/bloglist.html', {'page_obj': page_obj})

def blogDetail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'mainapp/blogdetail.html', {'blog': blog})

def mail(request):
    email = request.POST['email']
    suggestion = request.POST['mail-content']
    send_mail('',suggestion, email, ['mnnlthmpsn@outlook.com'])
    print('sending mail to %s' % email)
    return HttpResponseRedirect(reverse('mainapp:index'), {'message': 'hi'})