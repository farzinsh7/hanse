from django.contrib import admin
from .models import SiteInformation, SocialLinks, HelpfulLinks


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
