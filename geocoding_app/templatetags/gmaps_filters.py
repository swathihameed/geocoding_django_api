from django import template

register = template.Library()


@register.filter
def get_dict_value(dict_name, key):
    return dict_name[key]