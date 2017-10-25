from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^analyze/(?P<filename>\w{1,50})/$', views.analyze, name='analyze'),
    url(r'^post-to-sizer/(?P<filename>\w{1,50})/$', views.postToSizer, name='postToSizer'),
]