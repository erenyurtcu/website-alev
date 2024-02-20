from django.contrib import admin
from .models import PostModel, ContactModel, PostWorksModel

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_post')

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name','email','date_mail')

class PostWorksModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_post')

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(ContactModel, ContactModelAdmin)
admin.site.register(PostWorksModel, PostWorksModelAdmin)

