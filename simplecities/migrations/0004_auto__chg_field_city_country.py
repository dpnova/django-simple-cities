# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'City.country'
        db.alter_column('simplecities_city', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simplecities.Country']))


    def backwards(self, orm):
        
        # Changing field 'City.country'
        db.alter_column('simplecities_city', 'country_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['simplecities.Country']))


    models = {
        'simplecities.city': {
            'Meta': {'unique_together': "(['country', 'name'],)", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simplecities.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'simplecities.country': {
            'Meta': {'unique_together': "(['name', 'code_fips'], ['name', 'code_iso'])", 'object_name': 'Country'},
            'code_fips': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'code_iso': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tld': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'simplecities.location': {
            'Meta': {'unique_together': "(('country', 'city'),)", 'object_name': 'Location'},
            'city': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['simplecities.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simplecities.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['simplecities']
