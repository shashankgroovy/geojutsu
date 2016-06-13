from rest_framework import generics
from rest_framework_mongoengine import generics as drfme_generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from provider.models import Provider, GeoJsonPolygonFeature, \
        ServiceAreasFeatureCollection
from provider.serializers import ProviderSerializer, GeoJsonPolygonSerializer, \
        ServiceAreasSerializer



@api_view(['GET'])
def index(request, format=None):
    return Response({
        'Providers': reverse('provider-list', request=request, format=format),
        'ServiceAreas': reverse('serviceareasfeaturecollection-list', request=request, format=format)
    })



class ProviderList(drfme_generics.ListCreateAPIView):
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


class ProviderDetail(drfme_generics.RetrieveUpdateDestroyAPIView):
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



class ServiceAreasList(drfme_generics.ListCreateAPIView):
    """ Display list of all GeoJsonPolygonFeature features or creates a new
    feature collection of GeoJson Polygons.
    """

    queryset = ServiceAreasFeatureCollection.objects.all()
    serializer_class = ServiceAreasSerializer

    def get(self, request, *args, **kwargs):
        """Return a list of all feature collections when request method is
        GET."""
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        """Create new FeatureCollection of service areas"""
        return self.create(request, *args, **kwargs)


class ServiceAreaDetail(drfme_generics.GenericAPIView):
    """
    Retrieve, update or delete a specific FeatureCollection instance.
    """

    queryset = ServiceAreasFeatureCollection.objects.all()
    serializer_class = ServiceAreasSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class GeoJsonPolygonDetail(drfme_generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a specific GeoJsonPolygon instance.
    """

    queryset = ServiceAreasFeatureCollection.objects.all()
    serializer_class = ServiceAreasSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
