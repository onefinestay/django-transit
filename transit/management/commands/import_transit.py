from django.core.management.base import BaseCommand

from transit.importers.base import Importer
from transit.conf import DATA_FILES


class Command(BaseCommand):
    option_list = BaseCommand.option_list

    def handle(self, *args, **options):
        for path in DATA_FILES:
            importer = Importer(path)
            importer.run()