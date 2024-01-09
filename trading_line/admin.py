from django.contrib import admin
from .models import Trading
from . import models


@admin.register(models.Trading)
class TradingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')