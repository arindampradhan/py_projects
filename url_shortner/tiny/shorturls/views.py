from django.views.generic.edit import CreateView
from .models import Link
from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.shortcuts import redirect


class LinkCreate(CreateView):
    # class Meta:
    model = Link
    fields = ['url']

    def form_valid(self, form):
        prev = Link.objects.filter(url=form.instance.url)
        if prev:
            return redirect("link_show", pk=prev[0].pk)
        return super(LinkCreate, self).form_valid(form)


class LinkShow(DetailView):
    model = Link


class RedirectToLongURL(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        short_url = kwargs['short_url']
        return Link.expand(short_url)
