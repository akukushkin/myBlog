from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_pupkin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ask.views.index'),
    url(r'^signup/$', 'ask.views.signup'),
    url(r'^login/$', 'ask.views.login'),
    url(r'^answer/$', 'ask.views.answer'),
    url(r'^index/best/$', 'ask.views.index', {'sort': 'best'}),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
