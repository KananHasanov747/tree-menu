from django.contrib import admin
from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "named_url"]


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", "menu", "url", "named_url"]
    list_filter = ["parent"]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
