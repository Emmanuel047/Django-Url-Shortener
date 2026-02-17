from django.contrib import admin
from .models import Links
# Register your models here.
@admin.register(Links)
class Linkadmin(admin.ModelAdmin):
    list_display = ['short_code', 'url', 'on_click']