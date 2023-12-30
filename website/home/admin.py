from django.contrib import admin
from .models import PostModel, ContactModel

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_post')

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name','email','date_mail')

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(ContactModel, ContactModelAdmin)

