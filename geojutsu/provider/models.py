from __future__ import unicode_literals

from django.db import models
from mongoengine import *

class Provider(Document):
    """
    The db model for provider.
    """
    name = StringField(max_length=80, required=True)
    email = EmailField(max_length=80)
    phone = IntField(max_length=13)
    language = StringField(max_length=20)
    currency = StringField(max_length=5)


class GeoJsonPolygonFeature(EmbeddedDocument):
    """
    A GeoJsonPolygonFeature is an individual service area of a provider and
    takes 2 properties: name and price

    """
    type = StringField(default="Feature")
    geometry = PolygonField()
    properties = DictField()


class ServiceAreasFeatureCollection(Document):
    """
    A service area is a feature collection of individual features which are
    geojson polygons, and has a reference to the provider
    """
    provider = ReferenceField(Provider)
    type = StringField(default="FeatureCollection")
    features = ListField(EmbeddedDocumentField(GeoJsonPolygonFeature))
