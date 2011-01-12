from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/setlang/$', 'django.views.i18n.set_language'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'', include('cms.urls')),
)