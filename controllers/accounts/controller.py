from house.models import House
from accounts.models import Accounts
from rents.models import Rents


def profile_controller(user):
    if user.is_owner:
        try:
            query_set = House.objects.filter(
                created_by=Accounts.objects.get(username=user.username).id)
            return {"objects": query_set}
        except Exception as error:
            print('Error in profile_controller(owner) -->', error)
    elif user.is_tenant:
        try:
            rent = Rents.objects.get(tenant=user)
            return {"rent": rent}
        except Exception as error:
            print('Error in profile_controller(tenant) -->', error)

    return {}


def profile_view_controller(username):
    try:
        user = Accounts.objects.get(username=username)
        return {"view": True, "account": user}
    except Exception as error:
        print('Error in profile_view_controller -->', error)
        return {}
