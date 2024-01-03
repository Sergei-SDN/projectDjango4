from django import template

from django.conf import settings

register = template.Library()


@register.filter()
def mediapath(image_path):
    if image_path:
        # return f"{settings.MEDIA_URL}{image_path}"
        return f'/media/{image_path}'
    return '#'
