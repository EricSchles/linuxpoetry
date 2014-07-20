from django.conf.urls import patterns, url
from linuxpoetry import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.index, name='post'),
    url(r'^rss/$', views.PoetryFeed(), name="rss"),
    url(r'^blog/$', views.blogindex, name='blogindex'),
    url(r'^blog/(?P<post_id>\d+)/$', views.blogindex, name='blogpost'),
    url(r'^license/$', views.license, name='license'),
)
