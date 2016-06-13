from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from provider import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^providers/$', views.ProviderList.as_view(),
        name='provider-list'),

    url(r'^providers/(?P<pk>[0-9]+)/$', views.ProviderDetail.as_view(),
        name='provider-detail'),

    url(r'^serviceareas/$', views.ServiceAreasList.as_view(),
        name='serviceareasfeaturecollection-list'),

    url(r'^serviceareas/(?P<pk>[0-9]+)/$', views.ServiceAreaDetail.as_view(),
        name='serviceareasfeaturecollection-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
