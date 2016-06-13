"""
Our RESTful APi needs to provide the `Providers` and `ServiceAreas` as json
representations. Thus we need to provide a way of serializing and deserializing
the specific instances.
"""

from rest_framework_mongoengine.serializers import DocumentSerializer, \
        EmbeddedDocumentSerializer
from provider.models import Provider, ServiceAreasFeatureCollection, \
        GeoJsonPolygonFeature

from mongoengine import *

class ProviderSerializer(DocumentSerializer):
    """Declaring a provider serializer that works very similar to Django's native
    form"""

    pk = IntField(unique=True)
    class Meta:
        model = Provider
        depth = 2

    def create(self, validated_data):
        """
        Create and return a new `Provider` instance, given the validated data.
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


class GeoJsonPolygonSerializer(EmbeddedDocumentSerializer):
    """Declaring a geojson polygon serializer."""

    class Meta:
        model = GeoJsonPolygonFeature
        depth = 2


    def update(self, instance, validated_data):
        """
        Update and return an existing `GeoJsonPolygonFeature` instance, given
        the validated data.
        """
        instance.type = validated_data.get('type', instance.type)
        instance.geometry = validated_data.get('geometry', instance.geometry)
        instance.properties = validated_data.get('properties', instance.properties)
        instance.save()
        return instance


class ServiceAreasSerializer(DocumentSerializer):
    """Declaring a Feature collection serializer for geojson polygons."""

    provider = ReferenceField(Provider)
    features = GeoJsonPolygonSerializer(many=True)

    class Meta:
        model = ServiceAreasFeatureCollection
        depth = 2

    def create(self, validated_data):
        """Create and add GeoJson Polygon features to Service Area feature
        collection of provider"""
        features = validated_data.pop('features')
        featureCollection = ServiceAreasFeatureCollection.objects.create(**validated_data)
        featureCollection.features = []

        for feature in features:
            featureCollection.features.append(feature)
        featureCollection.save()

        return featureCollection

    def update(self, instance, validated_data):
        features = validated_data.pop('features')
        updated_instance = super(ServiceAreasSerializer, self).update(instance, validated_data)

        for feature in features:
            updated_instance.features.append(GeoJsonPolygonFeature(**feature))

        updated_instance.save()
        return updated_instance
