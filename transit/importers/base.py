import json

from django.contrib.gis.geos import Point

from .. import models


class Importer(object):

    def __init__(self, path):
        self.path = path

    def run(self):
        f = open(self.path)
        data = json.loads(f.read())
        self.process(data)

    def process(self, data):
        network_name = data['network']['name']
        network, __ = models.Network.objects.get_or_create(name=network_name)

        for line_data in data['lines']:
            line, __ = models.Route.objects.get_or_create(
                name=line_data['name'],
                short_name=line_data['short_name'],
                source_id=line_data['id'],
                color=line_data['colour'],
                network=network,
            )

        for station_data in data['stations']:
            station, __ = models.Station.objects.get_or_create(
                name=station_data['name'],
                source_id=station_data['id'],
                position=Point(float(station_data['longitude']), float(station_data['latitude']))
            )

            station.routes.clear()

            for line_data in station_data['lines']:
                route = models.Route.objects.get(network=network, source_id=line_data['line_id'])
                models.RouteStation.objects.create(
                    route=route,
                    station=station,
                )
