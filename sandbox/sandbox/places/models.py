from django.contrib.gis.db import models
from transit.models import Station

class Place(models.Model):
    name = models.CharField(max_length=255)
    position = models.PointField()

    objects = models.GeoManager()

    def nearest_stations(self):
        return Station.objects.distance(self.position).prefetch_related('routes').order_by('distance')[:5]

    def nearest_stations_mysql(self):
        return Station.objects.prefetch_related('routes').extra(
            select={
            'distance': '''(6371 * acos(
                            cos(radians(%s))
                            * cos(radians(Y(position)))
                            * cos(radians(X(position)) - radians(%s))
                            + sin(radians(%s))
                            * sin(radians(Y(position)))
                            ))'''
            },
            select_params=(self.position.y, self.position.x, self.position.y)
        ).order_by('distance')[:5]
