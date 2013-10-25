from django.contrib import admin
from . import models


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name',)


class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'network')
    list_filter = ('network',)


class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'list_routes')
    list_filter = ('routes', 'routes__network')

    def list_routes(self, obj):
        return u', '.join([unicode(x) for x in obj.routes.all()])
    list_routes.short_description = 'Routes'


admin.site.register(models.Network, NetworkAdmin)
admin.site.register(models.Route, RouteAdmin)
admin.site.register(models.Station, StationAdmin)