import random
from django.test import TestCase
from django.utils.text import slugify


from accounts.models import Accounts
from .models import House
from controllers.houses.controller import house_detail_controller, house_search_controller
from controllers.houses.utils import slugify_instance_title


class HouseTestCase(TestCase):

    def setUp(self):
        self.number_of_users = 5

        for i in range(0, self.number_of_users):

            owner = Accounts.objects.create(
                username=f'user_{i}',
                email=f'user_{i}@gmail.com',
                password='keySecret@761819',
                is_owner=True,
                is_tenant=False,
                full_name=f'user name {i}',
                phone=f'(555)-123-4567',
            )
            house = House.objects.create(
                title=f'title {i}',
                address=f'address {i}',
                price=random.randint(100, 10000) * random.random(),
                created_by=Accounts.objects.get(username=f'user_{i}'),
            )

    def test_queryset_exists(self):
        qs = House.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = House.objects.all()
        self.assertEqual(qs.count(), self.number_of_users)

    def test_house_search(self):
        for i in range(0, self.number_of_users):
            house_q = house_search_controller(
                {"q": f'address {i}'}).get('house_objects')
            house_r = House.objects.filter(address__contains=f'address {i}')
            self.assertEqual(house_q.count(), house_r.count())
