from django.core.management.base import BaseCommand, CommandError

from apps.currency.models import Currency


class Command(BaseCommand):
    help = "Update or view currency data"

    def add_arguments(self, parser):
        parser.add_argument('--id', type=int, help="Currency ID")
        parser.add_argument('--value', type=float, help="New currency value")

    def handle(self, *args, **options):
        currency_id = options.get('id')
        new_value = options.get('value')

        if currency_id and new_value:
            try:
                currency = Currency.objects.get(id=currency_id)
                currency.rate = new_value
                currency.save()
                self.stdout.write(self.style.SUCCESS(
                    f"Currency {currency.name} updated successfully "
                    f"with new value {new_value}."
                ))
            except Currency.DoesNotExist:
                raise CommandError(f"Currency with ID {currency_id} does not exist.")
        elif currency_id is not None:
            try:
                currency = Currency.objects.get(id=currency_id)
                self.stdout.write(
                    f"Currency ID: {currency.id}, Name: {currency.name}, "
                    f"Rate: {currency.rate}, Published Date: {currency.published_date}"
                )
            except Currency.DoesNotExist:
                raise CommandError(f"Currency with ID {currency_id} does not exist.")
        else:
            self.stdout.write(self.style.WARNING(
                'No currency ID and value provided. Use --id and --value to update '
                'or --id to view currency data.'
            ))
