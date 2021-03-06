from django.conf import settings


DATA_FILES = getattr(settings, 'TRANSIT_DATA_FILES', (
    'FR/PAR/metro.json',
    'FR/PAR/rer.json',
    'FR/PAR/tramway.json',
    'GB/LON/tube.json',
    'GB/LON/overground.json',
    'US/NYC/subway.json',
))