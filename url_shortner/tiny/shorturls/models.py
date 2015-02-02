from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

from .short import decimal2base_n, base_n2decimal


class Link(models.Model):
    url = models.URLField()

    def get_absolute_url(self):
        return reverse("link_show", kwargs={"pk": self.pk})

    def short_url(self):
        return reverse("redirect_short_url",
                       kwargs={"short_url": Link.shorten(self)})

    @staticmethod
    def shorten(link):
        l, _ = Link.objects.get_or_create(url=link.url)
        return str(decimal2base_n(l.pk))

    @staticmethod
    def expand(slug):
        link_id = int(base_n2decimal(slug))
        l = Link.objects.get(pk=link_id)
        return l.url
