from django.conf import settings


DATA_FILES = getattr(settings, 'TRANSIT_DATA_FILES', (
    'FR/PAR/metro.json',
    'GB/LON/tube.json',
))