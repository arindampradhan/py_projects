from django.conf.urls import patterns, include, url
from .views import results,tool
from .api import ToolResource

urlpatterns = patterns('',
    url(r'^$', 're_query_tool.views.tool', name='home'),
    url(r'^results/(?P<id>\d+)$', 're_query_tool.views.results', name='results'),
    url(r'^api/', include(ToolResource().urls)),
)
