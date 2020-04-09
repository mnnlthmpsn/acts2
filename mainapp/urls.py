from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blogs/', views.listBlogContent, name='blog_list'),
    path('blog/<int:blog_id>/detail/', views.blogDetail, name='blog_detail'),
    path('comment/<int:blog_id>/', views.comment, name='comment'),
    path('contact/', views.contact, name='contact'),
    path('mail/', views.mail, name='send_mail'),
]