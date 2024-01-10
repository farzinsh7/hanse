from modeltranslation.translator import TranslationOptions, register
from .models import Trading

@register(Trading)
class TradingTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'keywords', 'seo_description']