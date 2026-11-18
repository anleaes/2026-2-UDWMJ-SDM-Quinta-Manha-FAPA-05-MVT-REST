from django                        import template
from django.utils.html             import format_html
from django.db.models.fields.files import FieldFile

import os

register = template.Library()

@register.simple_tag
def file_link(file: FieldFile | None) -> str:
    if not file or not file.name:
        return ""

    # NOTE: File name without path and extension
    display_name = os.path.splitext(os.path.basename(file.name))[0]

    return format_html(
            '<a href="{}" class="text-link">{}</a>',
            file.url,
            display_name
        )
