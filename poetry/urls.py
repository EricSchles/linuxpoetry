import os

from django.conf.urls import patterns, include, url
#import linuxpoetry.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponse


def index(request):
    return HttpResponse("Sorry, linux-poetry.com is down for the time being.  - winter2718@gmail.com")

urlpatterns = patterns(
    '',
    url(r'^', index),
    #url(r'^', include(linuxpoetry.urls)),
)

if os.environ.get('POETRY_ADMIN') == '1':
    urlpatterns += url(r'^manage/admin/', include(admin.site.urls)),
