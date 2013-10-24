import json

from .. import models


class Importer(object):

    def __init__(self, path):
        self.path = path

    def run(self):
        f = open(self.path)
