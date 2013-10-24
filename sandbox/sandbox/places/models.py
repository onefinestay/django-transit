from django.contrib.gis.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    position = models.PointField()

    objects = models.GeoManager()