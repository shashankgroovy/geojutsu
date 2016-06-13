from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from provider import views

urlpatterns = [
    url(r'^$', views.provider_list),
    url(r'^providers/(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$', views.provider_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
