from rest_framework import serializers

from core.models import Tag, Store_link


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag subject"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class Store_linkSerializer(serializers.ModelSerializer):
    """Serializer for Ingredient objects"""

    class Meta:
        model = Store_link
        fields = ('id', 'name')
        read_only_fields = ('id',)
