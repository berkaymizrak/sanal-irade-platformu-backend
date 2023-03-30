from django.conf import settings
from django.utils.translation import get_language


def get_translation(obj, parameter):
    return obj.safe_translation_getter(
        parameter, default=obj.safe_translation_getter(parameter, language_code=settings.LANGUAGE_CODE),
        language_code=get_language() or settings.LANGUAGE_CODE
    )
