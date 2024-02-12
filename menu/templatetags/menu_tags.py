from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent=None)
    html = '<ul>'
    for item in menu_items:
        html += '<li>'
        html += f'<a href="{item.url}">{item.title}</a>'
        html += draw_children(item)
        html += '</li>'
    html += '</ul>'
    return html


def draw_children(parent_item):
    children = parent_item.children.all()
    if children:
        html = '<ul>'
        for child in children:
            html += '<li>'
            html += f'<a href="{child.url}">{child.title}</a>'
            html += draw_children(child)
            html += '</li>'
        html += '</ul>'
        return html
    else:
        return ''
