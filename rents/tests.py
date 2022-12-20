import datetime
import random
from django.test import TestCase


from .models import Rents
from house.models import House
from accounts.models import Accounts
from controllers.rents.controller import rent_view_controller


class RentTestCase(TestCase):
    def setUp(self):
        self.number_of_users = 4  # double
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

    def test_rent_controller(self):
        pass
    """
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

            temp_house = house
            q_title = house.title

            rent = Rents.objects.create(
                owner=house.created_by.username,
                tenant=Accounts.objects.get(username=f'user_{i}'),
                date_rented=datetime.date.today(),
                last_payment_date=datetime.date.today(),
                price=house.price,
                title=house.title,
            )

            q_account = rent.tenant

            house = House.objects.create(
                title=temp_house.title,
                address=temp_house.address,
                price=temp_house.price,
                rooms=temp_house.rooms,
                kitchen=temp_house.kitchen,
                washroom=temp_house.washroom,
                balcony=temp_house.balcony,
                created_by=temp_house.created_by
            )

            result = rent_view_controller(q_title, q_account)
            print("result", result)
            print("rent", rent)
            self.assertEqual(rent, result)
"""
