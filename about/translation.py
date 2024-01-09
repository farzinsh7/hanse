from modeltranslation.translator import TranslationOptions, register
from .models import AboutCompany

@register(AboutCompany)
class AboutCompanyTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'ceo_position', 'quote', 'keywords', 'seo_description']