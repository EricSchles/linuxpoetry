from django.shortcuts import render_to_response
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from poetry.settings import SITE_ROOT, STATIC_URL
from linuxpoetry.models import Post, BlogPost, BlogPostTag


def render_post(request, post_id=None, template_name=None, post_qs=None, section=None):
    post = None
    next_id = None
    prev_id = None
    post_qs = post_qs.order_by('-created_at')
    post_count = post_qs.count()
    if post_count > 0:
        if not post_id:
            post = post_qs[0]
            if post_count > 1:
                prev_id = post_qs[1].id
        else:
            post_found = False
            for p in post_qs:
                if post_found is True:
                    prev_id = p.id
                    break
                elif int(p.id) == int(post_id):
                    post = p
                    post_found = True
                if post_found is False:
                    next_id = p.id

    return render_to_response(
        template_name,
        {
            'request': request,
            'post': post,
            'next_id': next_id,
            'prev_id': prev_id,
            'static_url': STATIC_URL,
            'section': section
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


def blogsection(request, section, post_id=None):
    post_qs = BlogPostTag.objects.get(name=section).blogpost_set
    return render_post(
        request,
        post_id,
        template_name='linuxpoetry/blogsection.html',
        post_qs=post_qs,
        section=section
    )


def license(request):
    with open(SITE_ROOT + "/license.txt") as license_text:
        return HttpResponse(license_text.read().replace("\n", "<br/>"))


class PoetryFeed(Feed):
    title = "Linux Poetry RSS"
    link = "/"
    description = "Updates on the latest Linux poems."

    def items(self):
        return Post.objects.order_by('-id')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return "tags: %s" % item.tags_str

    def item_link(self, item):
        return reverse("post", args=[item.pk])


class MozillaFeed(Feed):
    title = "Linux Poetry's Mozilla Blog"
    link = "/blog/section/mozilla"
    description = "Any Mozilla related blogposts."

    def items(self):
        return BlogPostTag.objects.get(name='mozilla').blogpost_set.order_by('-id')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return '....'

    def item_link(self, item):
        return reverse("blogsectionpost", args=['mozilla', item.pk])
