from django.urls import path
from . import views

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "ALEV DUMANLIOĞLU"


urlpatterns = [
    path("", views.home, name="home"),
    path("", views.home),
    path("biyografi", views.about, name="about"),
    path("makaleler", views.blog, name="blog"),
    path("makale-<int:pk>/" , views.post_detail, name="postdetail"),
    path("iletisim", views.contact, name="contact"),
    path('x/', views.e_mail_sent, name='e-mail-sent'),
    path("calismalar", views.works, name="works"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
