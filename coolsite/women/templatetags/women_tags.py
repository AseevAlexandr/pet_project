from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name="get_cats")
def get_categories():
    return Category.objects.all()

