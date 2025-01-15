from rest_framework import serializers
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


class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = "__all__"


class DisadvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disadvantage
        fields = "__all__"


class ChoiceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceName
        fields = "__all__"


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagDetail
        fields = "__all__"


# Základní serializér pro SubGroup
class SubGroupBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGroup
        fields = "__all__"


# Rozšířený serializér pro SubGroup s relacemi
class SubGroupDetailedSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField()  # Vrací textové zobrazení Group
    advantages = serializers.StringRelatedField(many=True)  # ManyToManyField
    disadvantages = serializers.StringRelatedField(many=True)  # ManyToManyField
    env = serializers.StringRelatedField()  # ForeignKey
    env_secondary = serializers.StringRelatedField(many=True)  # ManyToManyField
    potential = serializers.StringRelatedField()  # ForeignKey
    size = serializers.StringRelatedField()  # ForeignKey
    difficulty_of_implementation = serializers.StringRelatedField()  # ForeignKey
    quantification = serializers.StringRelatedField()  # ForeignKey
    time_horizon = serializers.StringRelatedField()  # ForeignKey
    conflict = serializers.StringRelatedField(many=True)  # ManyToManyField
    tag = serializers.StringRelatedField()  # ForeignKey
    sdg = serializers.StringRelatedField(many=True)  # ManyToManyField
    unit = serializers.StringRelatedField()  # ForeignKey

    class Meta:
        model = SubGroup
        fields = "__all__"


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__"
