from django.contrib import admin
from .models import Blog, Event, Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Event)
admin.site.register(Comment)