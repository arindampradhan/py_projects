# from django.views.generic.edit import CreateView
# from .models import Link


class LinkCreate(CreateView):

    class Meta:
        model = Link
        fields = ['url']
