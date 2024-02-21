import time
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import PostModel,PostWorksModel
from .forms import ContactForm
from django.core.mail import send_mail
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
            send_mail(  'Your message has been received',
                        'Thank you for contacting us. We have received your message.',
                        'djangosmtpdeneme@gmail.com',
                        [form.cleaned_data['email']])
            
            send_mail(
                'Websitenizde Yeni Bir İletişim Talebi',
                f'İsim: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\nKonu: {form.cleaned_data["subject"]}\nMesaj: {form.cleaned_data["content"]}',
                'djangosmtpdeneme@gmail.com', 
                ['djangosmtpdeneme@gmail.com'], 
            )

            return redirect('e-mail-sent')
    else:
        form = ContactForm()

    return render(request, "contact.html", {'form': form, 'navbar': 'contact'})


def post_detail(request,pk):
    post = PostModel.objects.get(id=pk)
    context = {
        'post': post,
        'navbar': 'blog',
    }
    return render(request, "blog/post-detail.html", context)

def e_mail_sent(request):
    return render(request,"e-mail-sent/e-mail-sent.html")

def works(request):
    works = PostWorksModel.objects.all() 
    return render(request,"works/works.html",{'works': works ,'navbar': 'works'})

def works_detail(request,pk):
    work = PostWorksModel.objects.get(id=pk)
    context = {
        'work': work,
        'navbar': 'works',
    }
    return render(request, "works/work-detail.html", context)



