# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'Country', fields ['name', 'code_iso']
        db.create_unique('simplecities_country', ['name', 'code_iso'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Country', fields ['name', 'code_iso']
        db.delete_unique('simplecities_country', ['name', 'code_iso'])


    models = {
        'simplecities.city': {
            'Meta': {'unique_together': "(['country', 'name'],)", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simplecities.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'simplecities.country': {
            'Meta': {'unique_together': "(['name', 'code_fips'], ['name', 'code_iso'])", 'object_name': 'Country'},
            'code_fips': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'code_iso': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tld': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['simplecities']
