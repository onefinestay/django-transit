# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Network'
        db.create_table(u'transit_network', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'transit', ['Network'])

        # Adding model 'Route'
        db.create_table(u'transit_route', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('network', self.gf('django.db.models.fields.related.ForeignKey')(related_name='routes', to=orm['transit.Network'])),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal(u'transit', ['Route'])

        # Adding model 'RouteStation'
        db.create_table(u'transit_routestation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transit.Route'])),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transit.Station'])),
        ))
        db.send_create_signal(u'transit', ['RouteStation'])

        # Adding model 'Station'
        db.create_table(u'transit_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'transit', ['Station'])


    def backwards(self, orm):
        # Deleting model 'Network'
        db.delete_table(u'transit_network')

        # Deleting model 'Route'
        db.delete_table(u'transit_route')

        # Deleting model 'RouteStation'
        db.delete_table(u'transit_routestation')

        # Deleting model 'Station'
        db.delete_table(u'transit_station')


    models = {
        u'transit.network': {
            'Meta': {'object_name': 'Network'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'transit.route': {
            'Meta': {'object_name': 'Route'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'routes'", 'to': u"orm['transit.Network']"}),
            'source_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'transit.routestation': {
            'Meta': {'object_name': 'RouteStation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transit.Route']"}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transit.Station']"})
        },
        u'transit.station': {
            'Meta': {'object_name': 'Station'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'routes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'stations'", 'to': u"orm['transit.Route']", 'through': u"orm['transit.RouteStation']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'source_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['transit']