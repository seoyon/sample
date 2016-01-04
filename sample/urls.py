from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from files.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page),
    url(r'^attach/(\d+)/$', download),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
)
