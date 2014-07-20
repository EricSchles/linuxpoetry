"""A simple poem model."""

from django.db import models


class BaseTag(models.Model):

    """Represents some tag which should be applied to a post."""

    name = models.CharField(max_length=120)
    description = models.TextField()
    # Used for sorting tags.
    cardinality = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class PostTag(BaseTag):
    pass


class BasePost(models.Model):

    """Represents a single poem/post."""

    title = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    @property
    def body_with_html(self):
        """Will return the body after swapping tabs and newlines with html."""
        return str(
            self.body
        ).replace('\n', '<br/>').replace('\t', ' ').replace('\r', '')

    @property
    def tags_str(self):
        """Returns a comma delimited list of tags."""
        return ', '.join([tag.name for tag in self.tags.all()])

    class Meta:
        abstract = True


class Post(BasePost):
    tags = models.ManyToManyField(PostTag)


class BlogPostTag(BaseTag):
    pass


class BlogPost(BasePost):
    tags = models.ManyToManyField(BlogPostTag)
