from django.conf.urls import patterns, url
from linuxpoetry import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.index, name='post'),
    url(r'^rss/$', views.PoetryFeed(), name="rss"),
    url(r'^blog/$', views.blogindex, name='blogindex'),
    url(r'^blog/(?P<post_id>\d+)/$', views.blogindex, name='blogpost'),
    url(r'^blog/section/(?P<section>\w+)/$', views.blogsection, name='blogsection'),
    url(r'^blog/section/(?P<section>\w+)/(?P<post_id>\d+)/$', views.blogsection, name='blogsectionpost'),
    url(r'^rss/mozilla/$', views.MozillaFeed(), name="rssmozilla"),
    url(r'^license/$', views.license, name='license'),
)
