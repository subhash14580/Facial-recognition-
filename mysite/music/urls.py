from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from mysite import settings
from . import views

urlpatterns = [
    url(r'^$', views.index,name = 'index'),
    url(r'^register/$', views.register,name = 'register'),
    url(r'^register/train/(?P<slug>[\w-]+)/$', views.video_feed, name = 'register_train'),
    url(r'index1$', views.home,name = 'index1'),
    url(r'^search$', views.search,name = 'search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)