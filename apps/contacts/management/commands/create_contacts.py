import logging
import random

from django.core.management.base import BaseCommand, CommandError, CommandParser
from apps.contacts.models import Contact
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Create contact name'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('amount', type=int, )

    def handle(self, *args, **options):
        amount_contact_name = options['amount']

        # logger = logging.getLogger('create_contacts')
        # logger.setLevel(logging.INFO)

        # logging.info(f'Amount of contacts before: {Contact.objects.count()}')

        for _ in range(amount_contact_name):
            contact = Contact(
                contact_name=fake.first_name(),
                phone_number=f'+380{random.randint(100000000, 999999999)}',
            )

            contact.save()

    # logging.info(f'Amount of contacts after: {Contact.objects.count()}')
