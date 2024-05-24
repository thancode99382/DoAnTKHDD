from django import template

register = template.Library()


@register.filter
def is_empty(value):
    if value == '' or value is None:
        return True
    return False
