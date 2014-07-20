from django.shortcuts import render_to_response
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from poetry.settings import SITE_ROOT, STATIC_URL
from linuxpoetry.models import Post, BlogPost


def render_post(request, post_id=None, blog=False, template_name=None, post_qs=None):
    post = None
    next_id = None
    prev_id = None
    post_count = post_qs.count()
    if post_count > 0:
        if not post_id:
            post = post_qs.order_by('-created_at')[0]
        else:
            post = post_qs.get(id=post_id)
        if post.id < post_count:
            next_id = post.id + 1
        if post.id > 1:
            prev_id = post.id - 1

    return render_to_response(
        template_name,
        {
            'request': request,
            'post': post,
            'next_id': next_id,
            'prev_id': prev_id,
            'static_url': STATIC_URL,
        }
    )


def index(request, post_id=None):
    return render_post(
        request,
        post_id,
        template_name='linuxpoetry/base.html',
        post_qs=Post.objects
    )


def blogindex(request, post_id=None):
    return render_post(
        request,
        post_id,
        template_name='linuxpoetry/blog.html',
        post_qs=BlogPost.objects
    )


def license(request):
    with open(SITE_ROOT + "/license.txt") as license_text:
        return HttpResponse(license_text.read().replace("\n", "<br/>"))


class PoetryFeed(Feed):
    title = "Linux Poetry RSS"
    link = "/"
    description = "Updates on the latest Linux poems."

    def items(self):
        return Post.objects.order_by('-id')[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return "tags: %s" % item.tags_str

    def item_link(self, item):
        return reverse("post", args=[item.pk])
