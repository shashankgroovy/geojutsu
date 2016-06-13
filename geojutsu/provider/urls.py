from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from provider import views

urlpatterns = [
    url(r'^$', views.provider_list),
    url(r'^providers/(?P<name>[0-9]+)$', views.provider_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)
