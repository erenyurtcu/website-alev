import time
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import PostModel,ContactModel
from .forms import ContactForm
# Create your views here.

def home (request):
    return render(request,"index.html",{'navbar': 'home'})

def about(request):
    return render(request,"about.html",{'navbar': 'about'})

def blog(request):
    posts = PostModel.objects.all() 
    return render(request,"blog/blog.html", {'posts': posts ,'navbar': 'blog'})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('e-mail-sent')
 
    else:
        form = ContactForm()
        context = {
        'form': form
    }
    return render(request,"contact.html",{'form': form,'navbar': 'contact'})

def post_detail(request,pk):
    post = PostModel.objects.get(id=pk)
    context = {
        'post': post,
        'navbar': 'blog',
    }
    return render(request, "blog/post-detail.html", context)

def e_mail_sent(request):
    return render(request,"e-mail-sent.html")

def works(request):
    return render(request,"works.html",{'navbar': 'works'})



