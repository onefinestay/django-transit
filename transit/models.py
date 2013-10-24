from django.contrib.gis.db import models
from django.db.models import Q


class Network(models.Model):
    name = models.CharField(max_length=255)


class Route(models.Model):
    source_id = models.IntegerField()  # From the source CSV
    name = models.CharField(max_length=255)
    network = models.ForeignKey('transit.Route', related_name='routes')
    color = models.CharField(max_length=7)


class RouteStation(models.Model):
    route = models.ForeignKey('transit.Route')
    station = models.ForeignKey('transit.Station')


class Station(models.Model):
    source_id = models.IntegerField()  # From the source CSV
    name = models.CharField(max_length=255)
    position = models.PointField()
    route = models.ManyToManyField(
        to=Route,
        related_name='stations',
        through=RouteStation,
        blank=True,
        null=True)

    objects = models.GeoManager()

