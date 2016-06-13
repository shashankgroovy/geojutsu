from rest_framework import generics
from rest_framework_mongoengine import generics as drfme_generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

import mongoengine

from provider.models import Provider, GeoJsonPolygon
from provider.serializers import ProviderSerializer, GeoJsonPolygonSerializer



@api_view(['GET'])
def index(request, format=None):
    return Response({
        'Providers': reverse('provider-list', request=request, format=format),
        'ServiceAreas': reverse('geojsonpolygon-list', request=request, format=format)
    })



class ProviderList(generics.ListCreateAPIView):
    """
    Lists all providers or creates a new provider.
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def get(self, request, *args, **kwargs):
        """Return a list of all providers when request method is 'GET'."""
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a specific provider instance.
    """
    queryset = Provider.objects()
    serializer_class = ProviderSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class GeoJsonPolygonList(generics.ListCreateAPIView):
    """ Display list of all GeoJsonPolygon features or creates a new
    instance of GeoJsonPolygon.
    """

    queryset = GeoJsonPolygon.objects.all()
    serializer_class = GeoJsonPolygonSerializer

    def get(self, request, *args, **kwargs):
        """Return a list of all feature of type GeoJsonPolygon when request method is
        GET."""
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        """Create new Feature of type GeoJsonPolygon"""
        return self.create(request, *args, **kwargs)


class GeoJsonPolygonDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a specific provider instance.
    """
    queryset = GeoJsonPolygon.objects()
    serializer_class = GeoJsonPolygonSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['GET'])
def findServiceArea(request, x, y, format=None):
    point = mongoengine.PointField([x,y])

    for loc in GeoJsonPolygon.objects.all():

        locations = loc.objects(point__geo_within=loc.geometry)

    return Response({
        "locations": locations
    })

