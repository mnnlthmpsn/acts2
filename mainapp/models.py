from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('Date Published')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title

class Event(models.Model):
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateTimeField('Event Date')
    url = models.CharField(max_length=1000, default='http://localhost:8000/static/mainapp/img/bg-img/10.jpg')

    def __str__(self):
        return self.description

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content