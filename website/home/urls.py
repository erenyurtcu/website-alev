from django.urls import path
from . import views

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "ALEV DUMANLIOĞLU"


urlpatterns = [
    path("", views.home, name="home"),
    path("", views.home),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("post-detail/<int:pk>/" , views.post_detail, name="postdetail"),
    path("contact", views.contact, name="contact"),
    path('e-mail-sent/', views.e_mail_sent, name='e-mail-sent'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
