import random
import datetime
from django.test import TestCase

from .models import Accounts
from rents.models import Rents
from house.models import House
from controllers.accounts.controller import profile_controller, profile_view_controller


class AccountTestCase(TestCase):
    def setUp(self):
        self.number_of_users = 50
        for i in range(0, self.number_of_users):
            Accounts.objects.create(
                username=f'user_{i}',
                email=f'user_{i}@gmail.com',
                password='keySecret@761819',
                is_owner=True,
                is_tenant=False,
                full_name=f'user name {i}',
                phone=f'(555)-123-4567',
            )

        for i in range(0+500, self.number_of_users+500):
            Accounts.objects.create(
                username=f'user_{i}',
                email=f'user_{i}@gmail.com',
                password='keySecret@761819',
                is_owner=False,
                is_tenant=True,
                full_name=f'user name {i}',
                phone=f'(555)-123-4567',
            )

    def test_tenant(self):
        for i in range(0, self.number_of_users):
            house = House.objects.create(
                title=f'title {i}',
                address=f'address {i}',
                price=random.randint(1000, 100000) * random.random(),
                created_by=Accounts.objects.get(username=f'user_{i}'),
            )
            rent = Rents.objects.create(
                owner=f'user_{i}',
                tenant=Accounts.objects.get(username=f'user_{i+500}'),
                date_rented=datetime.date.today(),
                last_payment_date=datetime.date.today(),
                price=house.price,
                title=house.title)
        username = rent.tenant.username
        user = Accounts.objects.get(username=username)

        self.assertTrue(username == user.username)

    def test_profile_controller_tenant(self):
        for i in range(0, self.number_of_users):
            house = House.objects.create(
                title=f'title {i}',
                address=f'address {i}',
                price=random.randint(1000, 100000) * random.random(),
                created_by=Accounts.objects.get(username=f'user_{i}'),
            )
            rent = Rents.objects.create(
                owner=f'user_{i}',
                tenant=Accounts.objects.get(username=f'user_{i+500}'),
                date_rented=datetime.date.today(),
                last_payment_date=datetime.date.today(),
                price=house.price,
                title=house.title)
            username = rent.tenant.username
            user = Accounts.objects.get(username=username)
            user_rent = profile_controller(user).get('rent')

            self.assertEqual(rent, user_rent)

    def test_owner(self):
        for i in range(0, self.number_of_users):
            house = House.objects.create(
                title=f'title {i}',
                address=f'address {i}',
                price=random.randint(1000, 100000) * random.random(),
                created_by=Accounts.objects.get(username=f'user_{i}'),
            )
        username = house.created_by.username
        user = Accounts.objects.get(username=username)

        self.assertTrue(username == user.username)

    def test_profile_controller_owner(self):
        for i in range(0, self.number_of_users):
            house = House.objects.create(
                title=f'title {i}',
                address=f'address {i}',
                price=random.randint(1000, 100000) * random.random(),
                created_by=Accounts.objects.get(username=f'user_{i}'),
            )
        username = house.created_by.username
        user = Accounts.objects.get(username=username)
        qs = profile_controller(user).get('objects')
        test_qs = House.objects.filter(created_by=user.id)

        self.assertEqual(qs.count(), test_qs.count())

    def test_profile_view_controller(self):
        for i in range(0, self.number_of_users):
            user_name = f'user_{i}'
            user_account = profile_view_controller(user_name).get('account')
            self.assertEqual(f'user_{i}@gmail.com', user_account.email)
