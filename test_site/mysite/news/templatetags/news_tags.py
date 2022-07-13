from django import template

from ..models import Category

register = template.Library()

@register.simple_tag()
def get_categories():
    # Возвращает все категории
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='world'):
    categories = Category.objects.all()
    return {"categories": categories, "arg1": arg1, "arg2": arg2}