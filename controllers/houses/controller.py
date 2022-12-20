
from house.models import House


def house_detail_controller(slug):
    try:
        query = House.objects.get(slug=slug)
        context = {
            'object': query,
        }
        return context
    except:
        query = None
    return {}


def house_search_controller(query_dict):
    try:
        query = query_dict.get("q")
    except:
        query = None
    house_objects = None
    if query is not None:
        try:
            house_objects = House.objects.filter(price__lte=query)
        except Exception as e:
            house_objects = House.objects.filter(address__contains=query)
        except:
            house_objects = None
    return {"house_objects": house_objects, }
