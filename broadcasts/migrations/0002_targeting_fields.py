# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BroadcastMessage.user_target'
        db.add_column(u'broadcasts_broadcastmessage', 'user_target',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'BroadcastMessage.url_target'
        db.add_column(u'broadcasts_broadcastmessage', 'url_target',
                      self.gf('django.db.models.fields.TextField')(default='.*'),
                      keep_default=False)

        # Adding field 'BroadcastMessage.title'
        db.add_column(u'broadcasts_broadcastmessage', 'title',
                      self.gf('django.db.models.fields.CharField')(default='(No Title)', max_length=50),
                      keep_default=False)

        # Adding field 'BroadcastMessage.show_frequency'
        db.add_column(u'broadcasts_broadcastmessage', 'show_frequency',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'BroadcastMessage.message_type'
        db.add_column(u'broadcasts_broadcastmessage', 'message_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'BroadcastMessage.creation_date'
        db.add_column(u'broadcasts_broadcastmessage', 'creation_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


        # Changing field 'BroadcastMessage.start_time'
        db.alter_column(u'broadcasts_broadcastmessage', 'start_time', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'BroadcastMessage.end_time'
        db.alter_column(u'broadcasts_broadcastmessage', 'end_time', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'BroadcastMessage.message'
        db.alter_column(u'broadcasts_broadcastmessage', 'message', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting field 'BroadcastMessage.user_target'
        db.delete_column(u'broadcasts_broadcastmessage', 'user_target')

        # Deleting field 'BroadcastMessage.url_target'
        db.delete_column(u'broadcasts_broadcastmessage', 'url_target')

        # Deleting field 'BroadcastMessage.title'
        db.delete_column(u'broadcasts_broadcastmessage', 'title')

        # Deleting field 'BroadcastMessage.show_frequency'
        db.delete_column(u'broadcasts_broadcastmessage', 'show_frequency')

        # Deleting field 'BroadcastMessage.message_type'
        db.delete_column(u'broadcasts_broadcastmessage', 'message_type')

        # Deleting field 'BroadcastMessage.creation_date'
        db.delete_column(u'broadcasts_broadcastmessage', 'creation_date')


        # Changing field 'BroadcastMessage.start_time'
        db.alter_column(u'broadcasts_broadcastmessage', 'start_time', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'BroadcastMessage.end_time'
        db.alter_column(u'broadcasts_broadcastmessage', 'end_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 28, 0, 0)))

        # Changing field 'BroadcastMessage.message'
        db.alter_column(u'broadcasts_broadcastmessage', 'message', self.gf('django.db.models.fields.CharField')(max_length=140))

    models = {
        u'broadcasts.broadcastmessage': {
            'Meta': {'ordering': "['-end_time']", 'object_name': 'BroadcastMessage'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 28, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'message_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'show_frequency': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'(No Title)'", 'max_length': '50'}),
            'url_target': ('django.db.models.fields.TextField', [], {'default': "'.*'"}),
            'user_target': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['broadcasts']