from django.contrib.gis.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    position = models.PointField()

    objects = models.GeoManager()

    def nearest_stations(self):
        from transit.models import Station
        return Station.objects.distance(self.position).prefetch_related('routes').order_by('distance')[:5]