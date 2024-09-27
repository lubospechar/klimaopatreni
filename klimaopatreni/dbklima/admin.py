from django.contrib import admin
from .models import (
    Localization,
    Group,
    SubGroup,
    Advantage,
    Disadvantage,
    ChoiceName,
    Choice,
    Tag,
    TagDetail,
)


class GroupInline(admin.TabularInline):
    model = Group
    extra = 2


class SubGroupInline(admin.TabularInline):
    model = SubGroup
    extra = 2
    fields = ("subgroup_name", "code", "abstract", "description")


@admin.register(Localization)
class LocalizationAdmin(admin.ModelAdmin):
    list_display = ("localization_name",)
    inlines = [GroupInline]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "group_name",
        "localization",
    )
    list_filter = ("localization",)
    inlines = [SubGroupInline]


@admin.register(SubGroup)
class SubGroupAdmin(admin.ModelAdmin):
    list_display = ("subgroup_name", "code", "group", "abstract", "env")
    search_fields = ("subgroup_name", "code", "group__group_name")
    list_filter = ("group", "group__localization")
    fieldsets = (
        (None, {"fields": ("group", "subgroup_name", "code")}),
        ("Popis opatření", {"fields": ("abstract", "description")}),
        ("Výhody a Nevýhody", {"fields": ("advantages", "disadvantages")}),
        (
            "Složka životního prostředí",
            {"fields": ("env", "env_secondary", "mix_localization")},
        ),
        (
            "Potenciál realizovatelnosti",
            {
                "fields": (
                    "potential",
                    "size",
                    "difficulty_of_implementation",
                    "conditions_for_implementation",
                )
            },
        ),
        (
            "Účinnost",
            {"fields": ("quantification", "time_horizon")},
        ),
        (
            "Interakce s dalšími opatřeními",
            {"fields": ("related", "conflict", "other_conflict")}
        )
    )
    ordering = ("group", "subgroup_name")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "env":
            kwargs["queryset"] = Choice.objects.filter(choice_name_id=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "env_secondary":
            kwargs["queryset"] = Choice.objects.filter(choice_name_id=1)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)
    list_filter = ("description",)
    ordering = ("description",)
    fieldsets = (
        (None, {"fields": ("description",), "description": "Zadejte popis výhody"}),
    )
    verbose_name = "Výhoda"
    verbose_name_plural = "Výhody"


@admin.register(ChoiceName)
class ChoiceNameAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "choice_name",
    )
    search_fields = ("choice_name",)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_name", "choice", "order", "description")
    search_fields = ("choice", "description")
    list_filter = ("choice_name",)
    ordering = ["choice_name", "order"]


@admin.register(Disadvantage)
class DisadvantageAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)
    list_filter = ("description",)
    ordering = ("description",)
    fieldsets = (
        (None, {"fields": ("description",), "description": "Zadejte popis nevýhody"}),
    )
    verbose_name = "Nevýhoda"
    verbose_name_plural = "Nevýhody"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("tag_name",)

@admin.register(TagDetail)
class TagDetailAdmin(admin.ModelAdmin):
    list_display = ("tag", "tag_detail")
    list_filter = ("tag",)
