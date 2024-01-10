from modeltranslation.translator import TranslationOptions, register
from .models import HomeData, Slider, Features, CustomersReview, SiteInformation, HelpfulLinks

@register(HomeData)
class HomeDataTranslationOptions(TranslationOptions):
    fields = ['title', 'about', 'vision', 'mission', 'values' ]


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@register(Features)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@register(CustomersReview)
class CustomersReviewTranslationOptions(TranslationOptions):
    fields = ['position', 'description']


@register(SiteInformation)
class SiteInformationTranslationOptions(TranslationOptions):
    fields = ['title', 'description', 'address']


@register(HelpfulLinks)
class HelpfulLinksTranslationOptions(TranslationOptions):
    fields = ['title']