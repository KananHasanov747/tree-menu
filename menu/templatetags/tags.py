from django import template
from ..models import Menu

register = template.Library()


@register.filter
def is_active(item, request):
    path = request.get_full_path()
    return item.get_url() == path


@register.inclusion_tag("tags/dropdown.html", takes_context=True)
def draw_dropdown(context, item):
    return {"item": item, "request": context["request"]}


@register.inclusion_tag("tags/menu.html", takes_context=True)
def draw_menu(context, slug):
    menu = Menu.objects.get(slug=slug)

    return {"menu": menu, "request": context["request"]}
