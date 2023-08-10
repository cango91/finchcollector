from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter(name="fix_color_name")
@stringfilter
def fix_color_name(value):
    """Template filter to put spaces between CamelCase capitals. Won't work if capital letters are sequential, i.e. `ThisIsABadString` will produce -> `This Is ABad String`
    Main purpose is to put spaces between HTML color names such as PaleTurquoise, BurlyWood, etc...

    Args:
        value (str): the string to put spaces between CamelCase

    Returns:
        str: Camel Case
    """
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', value)