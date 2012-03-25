from django.core.management.base import BaseCommand, CommandError
from simplecities.models import Country, City
import codecs
import csv

class Command(BaseCommand):
    args = '<cities_file_path countries_file_path>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        if args:
            cities_path = args[0]
            country_path = args[1]
        else:
            raise CommandError(
            """
Please grab these files:
    http://download.geonames.org/export/dump/countryInfo.txt
    http://download.geonames.org/export/dump/cities15000.zip

Then call this like:
    manage loadsimplecities /path/to/cities1000.txt /path/to/countryInfo.txt
            """
            )
        self.stdout.write("cities path:\t%s\ncountries path:\t%s\n" %
            (cities_path,country_path))

        self.load_countries(open(country_path,"rU"))
        self.load_cities(open(cities_path, "rU"))



    def load_countries(self,handle):

        reader = csv.DictReader(handle,delimiter="\t",
            fieldnames=['ISO', 'ISO3', 'ISO-Numeric', 'fips', 'Country',
            'Capital', 'Area(in sq km)', 'Population', 'Continent', 'tld',
            'CurrencyCode', 'CurrencyName', 'Phone', 'Postal Code Format',
            'Postal Code Regex', 'Languages', 'geonameid', 'neighbours',
            'EquivalentFipsCode'])
        for row in reader:
            if row['ISO'].startswith("#"): continue
            country,created = Country.objects.get_or_create(
                code_iso=row['ISO'],
                name=row['Country']
            )
            country.code_fips = row['fips']
            country.tld = row['tld']
            country.save()

    def load_cities(self,handle):
        names = ['geonameid','name','asciiname','alternatenames','latitude','longitude',
                'feature class','feature code','country code','cc2','admin1 code',
                'admin2 code','admin3 code','admin4 code','population','elevation',
                'dem','timezone','modification date']
        reader = csv.DictReader(handle,delimiter="\t",fieldnames=names)
        for row in reader:
            if not row['country code']: continue
            city, created = City.objects.get_or_create(
                name=row['name'],
                country=Country.objects.get(code_iso=row['country code'])
            )