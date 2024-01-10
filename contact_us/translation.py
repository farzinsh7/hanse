from modeltranslation.translator import TranslationOptions, register
from .models import ContactUS

@register(ContactUS)
class ContactUSTranslationOptions(TranslationOptions):
    fields = [ 'title', 'address']