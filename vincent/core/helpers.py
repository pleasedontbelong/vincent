from django.contrib.staticfiles.storage import staticfiles_storage
from django.template import Context

from jinja2 import contextfunction
from jingo import register
from crispy_forms import utils
from sorl.thumbnail.shortcuts import get_thumbnail
from sorl.thumbnail.helpers import ThumbnailError
from django_hosts.reverse import (reverse_full as host_reverse_full,
                                  reverse_host as host_reverse_host)


@register.function
def thumbnail(image_file, geometry_string, **options):
    """
    calls the get_thumbnail from sorl
    """
    options.setdefault('format', 'PNG')
    try:
        im = get_thumbnail(image_file, geometry_string, **options)
    except ThumbnailError:
         # @TODO default image
        im = None
    return im


@register.function
@contextfunction
def crispy(context, form, helper):
    """
    Renders the form using crispy_forms
    """
    return utils.render_crispy_form(form, helper, context)


@register.function
@contextfunction
def crispy_field(context, field, form, form_style="", **kwargs):
    return utils.render_field(field, form, form_style, Context(), **kwargs)


@register.function
def static(path):
    return staticfiles_storage.url(path)


@register.function
def reverse_full(host, *args, **kwargs):
    return host_reverse_full(host, *args, **kwargs)


@register.function
def reverse_host(host, *args, **kwargs):
    return host_reverse_host(host, *args, **kwargs)
