import os

from django.core.management.base import BaseCommand

from transit.importers.base import Importer
from transit.conf import DATA_FILES


class Command(BaseCommand):
    option_list = BaseCommand.option_list

    def handle(self, *args, **options):
        import transit
        path = os.path.dirname(transit.__file__)
        base_path = os.path.normpath(os.path.join(path, '..', 'data'))

        for path in DATA_FILES:
            full_path = os.path.join(base_path, path)
            print 'Importing {}'.format(full_path)
            importer = Importer(full_path)
            importer.run()