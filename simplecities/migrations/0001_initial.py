# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('simplecities_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code_fips', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('code_iso', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('tld', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('simplecities', ['Country'])

        # Adding unique constraint on 'Country', fields ['name', 'code_fips']
        db.create_unique('simplecities_country', ['name', 'code_fips'])

        # Adding model 'City'
        db.create_table('simplecities_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simplecities.Country'])),
        ))
        db.send_create_signal('simplecities', ['City'])

        # Adding unique constraint on 'City', fields ['country', 'name']
        db.create_unique('simplecities_city', ['country_id', 'name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'City', fields ['country', 'name']
        db.delete_unique('simplecities_city', ['country_id', 'name'])

        # Removing unique constraint on 'Country', fields ['name', 'code_fips']
        db.delete_unique('simplecities_country', ['name', 'code_fips'])

        # Deleting model 'Country'
        db.delete_table('simplecities_country')

        # Deleting model 'City'
        db.delete_table('simplecities_city')


    models = {
        'simplecities.city': {
            'Meta': {'unique_together': "(['country', 'name'],)", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simplecities.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'simplecities.country': {
            'Meta': {'unique_together': "(['name', 'code_fips'],)", 'object_name': 'Country'},
            'code_fips': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'code_iso': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tld': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['simplecities']
