# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.contrib.gis.geos import Point


class Migration(DataMigration):

    def forwards(self, orm):
        Place = orm['places.Place']

        # Apt Bar
        Place(
            name='Apt Bar',
            position=Point(-0.092727, 51.512805)
        ).save()

        # Club Colosseum
        Place(
            name='Club Colosseum',
            position=Point(-0.128177, 51.484638)
        ).save()

        # Bloomsbury House
        Place(
            name='Bloomsbury House',
            position=Point(-0.122658, 51.518201)
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
