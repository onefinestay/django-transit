from django.contrib.gis.db import models


class TransitQuerySet(models.query.GeoQuerySet):

    def transit(self, point=None, longitude=None, latitude=None):
        """
        point, longitude and latitude should be the string field names
        of the relevant fields of the model we're working with. We
        prefer point if possible, but can use separate longitude and latitude
        fields too.
        """


class TransitManager(models.GeoManager):
    queryset_class = TransitQuerySet

    def get_queryset_class(self):
        return self.queryset_class

    def get_query_set(self):
        return self.get_queryset_class()(self.model)