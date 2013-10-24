# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.contrib.gis.geos import Point


class Migration(DataMigration):

    def forwards(self, orm):
        Place = orm['places.Place']

        Place(
            name='Le Balajo',
            position=Point(2.372185, 48.853986)
        ).save()

        Place(
            name='Le Barrio Latino',
            position=Point(2.372442, 48.852339)
        ).save()

        Place(
            name='Club 79',
            position=Point(2.302148, 48.870794)
        ).save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.contrib.gis.db.models.fields.PointField', [], {})
        }
    }

    complete_apps = ['places']
    symmetrical = True
