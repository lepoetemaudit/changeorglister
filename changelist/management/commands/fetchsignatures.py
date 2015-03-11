from django.conf import settings
from django.core.management import BaseCommand
import requests
import time
from changelist.models import Signature, Petition

URL = 'https://api.change.org/v1/petitions/get_id'
GET_SIGNATURES = 'https://api.change.org/v1/petitions/%d/signatures'
PETITION = 'https://www.change.org/p/bbc-reinstate-jeremy-clarkson'
PETITION_ID = 3034476


class Command(BaseCommand):
    USAGE = """Usage: python manage.py fetchsignatures <petition_url>"""

    def handle(self, *args, **options):
        if len(args) != 1:
            print(self.USAGE)
            return

        petition_url = args[0]
        name = petition_url.split("/")[-1].replace('-', " ").title()
        print(name)


        resp = requests.get(URL, params={'petition_url': petition_url, 'api_key': settings.CHANGE_ORG_API_KEY})
        result = resp.json()
        if 'petition_id' not in result:
            print("Petition not found")
            return

        petition_id = result['petition_id']
        petition = Petition.objects.create(
            name=name,
            petition_id=result['petition_id'],
            url=petition_url
        )

        next_page = None

        while True:
            if not next_page:
                resp = requests.get(GET_SIGNATURES % petition_id, params={'api_key': settings.CHANGE_ORG_API_KEY})
            else:
                resp = requests.get(next_page, params={'api_key': settings.CHANGE_ORG_API_KEY})

            data = resp.json()
            if 'signatures' not in data:
                return

            for s in data['signatures']:
                Signature.objects.create(
                    petition=petition,
                    country=s['country_code'],
                    name=s['name'],
                    city=s['city']
                )

            next_page = data['next_page_endpoint']
            print("Completed page %d of %d" % (data['page'], data['total_pages']))
            time.sleep(0.5)
