"""
Our RESTful APi needs to provide the `Providers` and `GeoJsonPolygon` as json
representations. Thus we need to provide a way of serializing and deserializing
the specific instances.
"""

from rest_framework_mongoengine.serializers import DocumentSerializer
from provider.models import Provider, GeoJsonPolygon


from mongoengine import *

class ProviderSerializer(DocumentSerializer):
    """Declaring a provider serializer that works very similar to Django's native
    form"""

    class Meta:
        model = Provider
        depth = 2
        fields = ('id','name','email','phone','language','currency')


    def create(self, validated_data):
        """
        Create and return a new `GeoJsonPolygon` instance, given the validated
        data.
        """
        return Provider.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Provider` instance, given the validated
        data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.language = validated_data.get('language', instance.language)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.save()
        return instance


class GeoJsonPolygonSerializer(DocumentSerializer):
    """Declaring a geojson polygon serializer."""

    provider = ReferenceField(Provider)
    class Meta:
        model = GeoJsonPolygon
        depth = 2


    def create(self, validated_data):
        """
        Create and return a new `GeoJsonPolygon` instance, given the validated
        data.
        """
        return GeoJsonPolygon.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `GeoJsonPolygon instance, given
        the validated data.
        """
        instance.type = validated_data.get('type', instance.type)
        instance.geometry = validated_data.get('geometry', instance.geometry)
        instance.properties = validated_data.get('properties', instance.properties)
        instance.provider = validated_data.get('provider', instance.provider)
        instance.save()
        return instance
