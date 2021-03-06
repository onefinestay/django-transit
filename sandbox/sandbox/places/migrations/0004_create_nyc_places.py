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
            name='Club Cache',
            position=Point(-73.986334, 40.759218)
        ).save()

        Place(
            name='LQ Nightclub',
            position=Point(-73.973452, 40.754880)
        ).save()

        Place(
            name='Copacabana New York',
            position=Point(-73.987201, 40.760035)
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
