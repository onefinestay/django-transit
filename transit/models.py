from django.db import models, Q


class Network(models.Model):
    name = models.CharField(max_length=255)


class Route(models.Model):
    name = models.CharField(max_length=255)
    network = models.ForeignKey('transit.Route', related_name='routes')
    color = models.CharField(max_length=7)


class RouteStation(models.Model):
    route = models.ForeignKey('transit.Route')
    station = models.ForeignKey('transit.Station')


class Station(models.Model):
    name = models.CharField(max_length=255)
    position = models.PointField()

    route = models.ManyToMany(
        to=Route,
        related_name='stations',
        through=RouteStation,
        blank=True,
        null=True)
