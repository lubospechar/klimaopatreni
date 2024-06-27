from django.contrib import admin
from dbklima.models import Localization, Group

@admin.register(Localization)
class LocalizationAdmin(admin.ModelAdmin):
    list_display = ('localization_name',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'localization',)
    list_filter = ('localization', )
