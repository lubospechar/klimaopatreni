from django.contrib import admin
from .models import Localization, Group, SubGroup, Advantage, Disadvantage

class GroupInline(admin.TabularInline):
    model = Group
    extra = 2

class SubGroupInline(admin.TabularInline):
    model = SubGroup
    extra = 2
    fields = ('subgroup_name', 'code', 'abstract', 'description')

@admin.register(Localization)
class LocalizationAdmin(admin.ModelAdmin):
    list_display = ('localization_name',)
    inlines = [GroupInline]

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'localization',)
    list_filter = ('localization', )
    inlines = [SubGroupInline]

@admin.register(SubGroup)
class SubGroupAdmin(admin.ModelAdmin):
    list_display = ('subgroup_name', 'code', 'group', 'abstract')
    search_fields = ('subgroup_name', 'code', 'group__group_name')
    list_filter = ('group', 'group__localization')
    fieldsets = (
        (None, {
            'fields': ('group', 'subgroup_name', 'code')
        }),
        ('Popis opatření', {
            'fields': ('abstract', 'description')
        }),
        ('Výhody a Nevýhody', {
            'fields': ('advantages', 'disadvantages')
        }),
    )
    ordering = ('group', 'subgroup_name')

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ('description',)
    ordering = ('description',)
    fieldsets = (
        (None, {
            'fields': ('description',),
            'description': 'Zadejte popis výhody'
        }),
    )
    verbose_name = 'Výhoda'
    verbose_name_plural = 'Výhody'

@admin.register(Disadvantage)
class DisadvantageAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ('description',)
    ordering = ('description',)
    fieldsets = (
        (None, {
            'fields': ('description',),
            'description': 'Zadejte popis nevýhody'
        }),
    )
    verbose_name = 'Nevýhoda'
    verbose_name_plural = 'Nevýhody'
