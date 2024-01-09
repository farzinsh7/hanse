from django.contrib import admin
from .models import SiteInformation, SocialLinks, HelpfulLinks, HomeData, Slider, Features, CustomersReview, BrandImage


class SocialLinksAdmin(admin.TabularInline):
    model = SocialLinks
    extra = 1
    max_num = 10


class HelpfulLinksAdmin(admin.TabularInline):
    model = HelpfulLinks
    extra = 1
    max_num = 10


@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    inlines = [SocialLinksAdmin, HelpfulLinksAdmin]

#########---------HomeData--------------##########

class SliderAdmin(admin.TabularInline):
    model = Slider
    extra = 1
    max_num = 10

class FeaturesAdmin(admin.TabularInline):
    model = Features
    extra = 1
    max_num = 3

class CustomersReviewAdmin(admin.TabularInline):
    model = CustomersReview
    extra = 1
    max_num = 5

class BrandImageAdmin(admin.TabularInline):
    model = BrandImage
    extra = 1
    max_num = 5

@admin.register(HomeData)
class HomeDataAdmin(admin.ModelAdmin):
    inlines = [SliderAdmin, FeaturesAdmin, CustomersReviewAdmin, BrandImageAdmin]