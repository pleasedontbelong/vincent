from django.conf.urls import patterns, include, url
from django.conf import settings

import autocomplete_light
autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #autocompletes
    # url(r'^autocomplete/', include('autocomplete_light.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
                            url(r'^static/(?P<path>.*)$', 'serve'),
                            )
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}
                                ),
                            )

urlpatterns +=  (
    # Users
    url(r'^', include('users.urls')),
)
