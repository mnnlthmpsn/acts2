from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse
from django.core.files import File

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

def contact(request):
    return render(request, 'mainapp/contact.html')

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
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message'] + ' sent by:' + email
    try:
        send_mail(('message from %s' % name),message, email, ['info.actschapter2@gmail.com'])
        messages.add_message(request, messages.SUCCESS, 'Mail sent successfully')
    except:
        messages.add_message(request, messages.WARNING, 'Mail not sent')
    return HttpResponseRedirect(reverse('mainapp:contact'),)
