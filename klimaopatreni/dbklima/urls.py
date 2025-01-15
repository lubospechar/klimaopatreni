from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    LocalizationViewSet,
    GroupViewSet,
    AdvantageViewSet,
    DisadvantageViewSet,
    ChoiceNameViewSet,
    ChoiceViewSet,
    TagViewSet,
    TagDetailViewSet,
    SubGroupViewSet,
    SubGroupFullViewSet,
    ExampleViewSet,
    ModelMetadataViewSet,
)

# Inicializace routeru
router = DefaultRouter()

# Registrace ViewSetů
router.register("localizations", LocalizationViewSet, basename="localization")
router.register("groups", GroupViewSet, basename="group")
router.register("advantages", AdvantageViewSet, basename="advantage")
router.register("disadvantages", DisadvantageViewSet, basename="disadvantage")
router.register("choice-names", ChoiceNameViewSet, basename="choice-name")
router.register("choices", ChoiceViewSet, basename="choice")
router.register("tags", TagViewSet, basename="tag")
router.register("tag-details", TagDetailViewSet, basename="tag-detail")
router.register("subgroups", SubGroupViewSet, basename="subgroup")  # Základní endpoint
router.register(
    "subgroups-full", SubGroupFullViewSet, basename="subgroup-full"
)  # Detailní endpoint
router.register("examples", ExampleViewSet, basename="example")

# Nový endpoint pro metadata modelů
router.register("model-metadata", ModelMetadataViewSet, basename="model-metadata")

# Definice URL
urlpatterns = [
    path("api/", include(router.urls)),
]
