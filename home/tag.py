from django import template

register = template.Library()

@register.assignment_tag
def inx():

    
    return 1