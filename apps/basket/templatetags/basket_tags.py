from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def is_in_basket(context, course_id):
    basket = context['basket']
    for line in basket.basket.lines.all():
        if course_id == line.course.id:
            return True
    return False