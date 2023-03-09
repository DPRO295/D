# myapp/templatetags/my_tags.py

from django import template
import json

register = template.Library()

@register.simple_tag
def json_script(data):
    return '<script type="application/json">{}</script>'.format(json.dumps(data))