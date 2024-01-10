from modeltranslation.translator import TranslationOptions, register
from .models import Investment

@register(Investment)
class InvestmentTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'keywords', 'seo_description']