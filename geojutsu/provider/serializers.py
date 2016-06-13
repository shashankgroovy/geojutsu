"""
Our RESTful APi needs to provide the `Providers` and `ServiceAreas` as json
representations. Thus we need to provide a way of serializing and deserializing
the specific instances.
"""

from rest_framework_mongoengine.serializers import DocumentSerializer
from provider.models import Provider

class ProviderSerializer(DocumentSerializer):
    """Declaring a serializer that works very similar to Django's native
    form"""

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


