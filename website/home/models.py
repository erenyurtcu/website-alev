from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import SafeString




# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_post = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ('-date_post',)
        verbose_name_plural = "Makaleler"

    def __str__(self):
        return self.title
    
class PostWorksModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_post = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-date_post',)
        verbose_name_plural = "Çalışmalar"

    def __str__(self):
        return self.title
    


    

class ContactModel(models.Model):
    name = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 255)
    content = models.TextField()
    date_mail = models.DateTimeField(auto_now_add = True)
    

    class Meta:
        ordering = ('-date_mail',)
        verbose_name_plural = "İletişim Talepleri"

    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='widget-group'>"))


    def __str__(self):
        return self.name
    
