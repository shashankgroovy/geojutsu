from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from provider.models import Provider
from provider.serializers import ProviderSerializer

# wrapping our api with function based API views.
# therefore we use the `@api_view` decorator on our independent functions.

@api_view(['GET', 'POST'])
def provider_list(request, format=None):
    """
    List all providers or create a new provider.
    """
    if request.method == 'GET':
        # return a list of all providers when request method is 'GET'.
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        # Here instead of using Request object's `request.POST` attribute, we
        # use `request.data` which can handle more arbitary data and works for
        # 'POST', 'PUT' and 'PATCH' methods.

        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def provider_detail(request, name, format=None):
    """
    Retrieve, update or delete a specific provider instance.
    """
    try:
        # Filter provider by name
        provider = Provider.objects.get(name=name)
    except Provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProviderSerializer(provider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
