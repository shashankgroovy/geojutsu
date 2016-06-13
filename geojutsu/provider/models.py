from __future__ import unicode_literals

from django.db import models
from mongoengine import *

class Provider(Document):
    name = StringField(max_length=80)
    email = EmailField(max_length=80)
    phone = IntField(max_length=13)
    language = StringField(max_length=20)
    currency = StringField(max_length=5)
