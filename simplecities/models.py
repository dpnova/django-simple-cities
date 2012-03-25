
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Country(models.Model):
    name = models.CharField(max_length=50)
    code_fips = models.CharField(max_length=5)
    code_iso = models.CharField(max_length=5)
    tld = models.CharField(max_length=5)

    def __unicode__(self):
        return u"%s" % (self.name)


    class Meta:
        unique_together = (['name','code_fips'],['name','code_iso'])


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country)

    class Meta:
        unique_together = (['country','name'],)
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        return u"%s" % (self.name)



class Location(models.Model):
    country = models.ForeignKey(Country)
    city = ChainedForeignKey(
        City,
        chained_field="country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True
    )
    def __unicode__(self):
        return u"%s, %s" % (self.city.name, self.country.name)

