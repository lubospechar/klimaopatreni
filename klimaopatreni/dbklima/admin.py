from django.contrib import admin
from dbklima.models import Localization, Group, SubGroup

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
    )
    ordering = ('group', 'subgroup_name')
