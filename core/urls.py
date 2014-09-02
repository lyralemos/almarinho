from django.conf.urls import patterns, include, url

from views import EntryListView, EntryDetailView

urlpatterns = patterns('',
    url(r'^(?P<slug>[-_\w]+)/$', EntryDetailView.as_view(), name='entry-detail'),
    url(r'^$',EntryListView.as_view(),name='index'),
)