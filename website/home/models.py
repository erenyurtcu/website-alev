from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_post = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ('-date_post',)

    def __str__(self):
        return self.title
    

class ContactModel(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 255)
    content = models.TextField()
    date_mail = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-date_mail',)

    def __str__(self):
        return self.name
