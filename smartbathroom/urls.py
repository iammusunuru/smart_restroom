from django.conf.urls import patterns, include, url
import smartb
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smartbathroom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'smartb.views.home', name='home'),
    url(r'^loaddata', 'smartb.views.loaddata', name='loaddata'),
    url(r'^template', 'smartb.views.load_html', name='loadhtml'),
    url(r'^configure', 'smartb.views.send_sensor', name='send_sensor'),
    url(r'^noticonf', 'smartb.views.noti_config', name='noticonfig'),
    url(r'^washroom', 'smartb.views.get_active_washroom', name='active_room'),
    url(r'^admin/', include(admin.site.urls)),
)
