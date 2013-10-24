from django.db import models, Q


class Network(models.Model):
    name = models.CharField(max_length=255)


class Route(models.Model):
    network = models.ForeignKey('transit.Route', related_name='routes')


class RouteStation(models.Model):
    route = models.ForeignKey('transit.Route')
    station = models.ForeignKey('transit.Station')
    next = models.ForeignKey('transit.Station', related_name='+')
    previous = models.ForeignKey('transit.Station', related_name='+')


class Station(models.Model):
    name = models.CharField(max_length=255)
    position = models.PointField()

    route = models.ManyToMany(Route, related_name='stations', through=RouteStation)
