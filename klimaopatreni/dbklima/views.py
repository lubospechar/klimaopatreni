from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.apps import apps

from .models import (
    Localization,
    Group,
    Advantage,
    Disadvantage,
    ChoiceName,
    Choice,
    Tag,
    TagDetail,
    SubGroup,
    Example,
)
from .serializers import (
    LocalizationSerializer,
    GroupSerializer,
    AdvantageSerializer,
    DisadvantageSerializer,
    ChoiceNameSerializer,
    ChoiceSerializer,
    TagSerializer,
    TagDetailSerializer,
    SubGroupBasicSerializer,
    SubGroupDetailedSerializer,
    ExampleSerializer,
)


class LocalizationViewSet(ReadOnlyModelViewSet):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AdvantageViewSet(ReadOnlyModelViewSet):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer


class DisadvantageViewSet(ReadOnlyModelViewSet):
    queryset = Disadvantage.objects.all()
    serializer_class = DisadvantageSerializer


class ChoiceNameViewSet(ReadOnlyModelViewSet):
    queryset = ChoiceName.objects.all()
    serializer_class = ChoiceNameSerializer


class ChoiceViewSet(ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailViewSet(ReadOnlyModelViewSet):
    queryset = TagDetail.objects.all()
    serializer_class = TagDetailSerializer


# Základní ViewSet
class SubGroupViewSet(ReadOnlyModelViewSet):
    queryset = SubGroup.objects.all()
    serializer_class = SubGroupBasicSerializer


# Detailní ViewSet
class SubGroupFullViewSet(ReadOnlyModelViewSet):
    queryset = SubGroup.objects.all()
    serializer_class = SubGroupDetailedSerializer


class ExampleViewSet(ReadOnlyModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer


class ModelMetadataViewSet(ViewSet):
    """
    ViewSet pro zobrazení metadat modelů aplikace `dbklima`.
    """

    def list(self, request):
        app_name = "dbklima"
        metadata = []
        for model in apps.get_models():
            if model._meta.app_label == app_name:
                model_info = {
                    "class_name": model.__name__,
                    "model_name": model._meta.verbose_name,
                    "fields": [
                        {
                            "name": field.name,
                            "verbose_name": field.verbose_name,
                            "help_text": getattr(field, "help_text", ""),
                            "field_type": field.get_internal_type(),
                        }
                        for field in model._meta.get_fields()
                        if hasattr(field, "verbose_name")
                    ],
                }
                metadata.append(model_info)
        return Response(metadata)
