#!/usr/bin/env python
import json
import sys, os
from xml.etree import ElementTree as et
from BeautifulSoup import BeautifulSoup

NS = {'kml': 'http://www.opengis.net/kml/2.2'}

def get_network(doc):

    stations = list(get_stations(doc))
    lines = list(get_lines(stations))

    return {
        "network": {
            "name": "NYC Subway",
            "key": "nyc-subway"
        },
        "lines": lines,
        "stations": stations
    }


def get_lines(stations):
    collected = set()

    for station in stations:
        for line in station['lines']:
            line = line['line_id']
            if line not in collected:
                collected.add(line)
                yield {
                    "colour": "#000000",
                    "branches": [],
                    "id": line,
                    "short_name": line,
                    "name": line
                }


def get_stations(doc):
    for plcmrk in doc.findall('./kml:Document/kml:Placemark', NS):
        id_ = int(plcmrk.get('id').rsplit('.', 1)[1])

        lat = plcmrk.find('./kml:LookAt/kml:latitude', NS).text
        lon = plcmrk.find('./kml:LookAt/kml:longitude', NS).text

        descr = plcmrk.find('./kml:description', NS).text
        station = get_station_data(descr)

        yield {
            "interchanges": [],
            "name": station['name'],
            "lines": station['lines'],
            "longitude": lon,
            "latitude": lat,
            "id": id_
        }
        print 'processed station', station['name']

def get_station_data(descr):
    # description contains non-well-formed HTML with the actual information
    descr = str(BeautifulSoup(descr))
    descr = et.fromstring('<description>{}</description>'.format(descr))

    station = {}
    for li in descr.iter('li'):
        attr = li.find("./strong/span[@class='atr-name']").text.lower()
        val = li.find("./span[@class='atr-value']").text
        station[attr] = val


    station['lines'] = [
        {
            "line_id": line,
            "branches": []
        } for line in station.pop('line').split('-')
    ]

    return station




def main():
    kml_file = sys.argv[1]
    tree = et.parse(kml_file)
    root = tree.getroot()

    network = get_network(root)

    json_file, ext = os.path.splitext(kml_file)
    json_file = json_file + '.json'
    with open(json_file, 'wb') as fle:
        json.dump(network, fle, indent=4)



if __name__ == '__main__':
    main()