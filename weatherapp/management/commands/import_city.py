from datetime import datetime
from django.core.management import BaseCommand, CommandError
import geonamescache
from weatherapp.models import City


class Command(BaseCommand):
    help = 'Export City'

    def handle(self, *args, **options):
        try:
            created = updated = 0
            gc = geonamescache.GeonamesCache()
            cities = gc.get_cities()
            for key, value in cities.items():
                city,city_created = City.objects.update_or_create(name=value.get('name'), defaults={'country_code':value.get('countrycode')})
                print("[Success] - {}".format(city))
                if city_created:
                    created += 1
                else:
                    updated += 1
        except Exception as e:
            raise CommandError(e)
        self.stdout.write(self.style.SUCCESS('City {} created,{} updated'.format(created,updated)))
