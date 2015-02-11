from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Tool
from .forms import ToolForm
import json
import re


def tool(request):
    if request.method == "POST":
        form = ToolForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            string = temp.string
            pattern = temp.pattern
            matches = re.findall(pattern, string)
            match = json.dumps(matches)
            tool = Tool(string=string, pattern=pattern, match=match)
            tool.save()
            id = tool.id
            return HttpResponseRedirect(reverse('results', kwargs={'id': id}))
        else:
            print "\nERROR:\n", form.errors

    else:
        form = ToolForm()
    return render(request, 'index.html', locals())


def results(request, id=''):
    try:
        tool = Tool.objects.get(pk=id)
        matches = json.loads(tool.match)
    except:
        pass
    return render(request, 'results.html', locals())


def validate_len(value):
    if lne(value) == 0:
        raise ValidationError('%s is not even' % value)
