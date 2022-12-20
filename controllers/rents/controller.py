import datetime

from rents.models import Rents
from house.models import House


def rent_view_controller(query_title, request_user):
    try:
        print(0)
        rent_house = House.objects.get(title=query_title)
        print(1)
        rent_house_owner = rent_house.created_by.username
        print(2)
        rent_house_price = rent_house.price
        print(3)
        renting_date = datetime.date.today()
        print(4)

        rent_details = Rents.objects.create(
            owner=rent_house_owner,
            tenant=request_user,
            date_rented=renting_date,
            last_payment_date=renting_date,
            price=rent_house_price,
            title=query_title
        )
        print(5)
    except Exception as e:
        print('Error in rent_view_controller -->', e)
        return None

    return rent_details
