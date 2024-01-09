from django.contrib import admin
from .models import Investment
from . import models


@admin.register(models.Investment)
class InvestmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')