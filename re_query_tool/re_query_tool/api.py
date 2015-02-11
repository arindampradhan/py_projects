from tastypie.resources import ModelResource
from re_query_tool.models import Tool

class ToolResource(ModelResource):
    class Meta:
        queryset = Tool.objects.all()
        resource_name = 'tool'
        allowed_methods = ['get','post']