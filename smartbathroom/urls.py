from django.conf.urls import patterns, include, url
import smartb
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smartbathroom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'smartb.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
