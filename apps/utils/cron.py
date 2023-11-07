from datetime import datetime
import requests
import certifi
from django.conf import settings
import defusedxml.ElementTree as ET
from apps.currency.models import Currency


def fetch_and_update_currencies():
    certificate = certifi.where()
    url = settings.CURRENCY_GET_URL

    try:
        response = requests.post(url, verify=certificate)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"HTTP Request failed: {e}")

    try:
        data = ET.fromstring(response.content)
    except ET.ParseError as e:
        raise Exception(f"XML parsing failed: {e}")

    for currency_item in data.findall('.//item'):
        pub_date = currency_item.find('pubDate').text
        formatted_date_str = datetime.strptime(pub_date, '%d.%m.%Y').strftime('%Y-%m-%d')
        currency_name = currency_item.find('title').text
        currency_rate = float(currency_item.find('description').text)
        currency, created = Currency.objects.get_or_create(
            name=currency_name,
            defaults={'rate': currency_rate, 'published_date': formatted_date_str}
        )
        if not created:
            currency.rate = currency_rate
            currency.published_date = formatted_date_str
            currency.save()
    return 'Currency data updated successfully.'
