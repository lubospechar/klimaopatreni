from django.contrib import admin
from dbklima.models import Localization, Group

class GroupInline(admin.TabularInline):
    model = Group
    extra = 2  # Kolik prázdných řádků pro nový záznam se zobrazí

@admin.register(Localization)
class LocalizationAdmin(admin.ModelAdmin):
    list_display = ('localization_name',)
    inlines = [GroupInline]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'localization',)
    list_filter = ('localization', )
