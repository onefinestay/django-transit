from django.conf.urls import patterns, include, url

from .places import views


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.PlaceListView.as_view(), name='home'),
    # url(r'^sandbox/', include('sandbox.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
