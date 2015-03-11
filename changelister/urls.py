from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'changelist.views.list', name='home'),
    url(r'^(\d+)$', 'changelist.views.details', name='details'),


    url(r'^admin/', include(admin.site.urls)),
)
