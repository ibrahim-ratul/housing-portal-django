import datetime
import random
from django.test import TestCase


from .models import Rents
from house.models import House
from accounts.models import Accounts
from controllers.rents.controller import rent_view_controller


class RentTestCase(TestCase):
    def setUp(self):
        self.number_of_users = 4
        self.number_of_rents = 4

        for i in range(0, self.number_of_users):
            Accounts.objects.create(
                username=f'user_{i}',
                email=f'user_{i}@email.com',
                full_name=f'user {i}',
                phone=f'(555)-456-1234',
                is_tenant=True
            )

        for i in range(0, self.number_of_users):
            Accounts.objects.create(
                username=f'user_{i+400}',
                email=f'user_{i+400}@email.com',
                full_name=f'user {i+400}',
                phone=f'(555)-456-1234',
                is_owner=True
            )

        for i in range(0, self.number_of_users):
            house = House.objects.create(
                title=f'Title-{i}',
                address=f'Address, {i}',
                price=random.randint(10, 100_000) * random.random(),
                rooms=random.randint(1, 10),
                kitchen=random.randint(1, 10),
                washroom=random.randint(1, 10),
                balcony=random.randint(1, 10),
                created_by=Accounts.objects.get(username=f'user_{i+400}')
            )
            Rents.objects.create(
                owner=house.created_by.username,
                tenant=Accounts.objects.get(username=f'user_{i}'),
                date_rented=datetime.date.today(),
                last_payment_date=datetime.date.today(),
                price=house.price,
                title=house.title,
            )

    def test_rent_count(self):
        qs = Rents.objects.all()
        self.assertEqual(self.number_of_rents, qs.count())

    def test_tenant_count(self):
        qs = Rents.objects.all()
        self.assertEqual(self.number_of_users, qs.count())

    def test_house_count(self):
        qs = House.objects.all()
        self.assertEqual(0, qs.count())
