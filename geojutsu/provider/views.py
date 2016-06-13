from django.shortcuts import render
from django.http import HttpResponse


from mongoengine import *
from models import Provider

def index(request):
    # connect to db
    connect('mozio')

    provider = Provider.objects.create(
        name = 'John Doe',
        email = 'johndoe@mail.com',
        phone = '1234567890',
        language = 'English',
        currency = 'USD'
    )

    provider.save()

    providerlist = []
    for i in Provider.objects:
        providerlist.append((i.name, i.email))

    return HttpResponse(providerlist)
