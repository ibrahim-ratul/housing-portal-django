import random
from django.utils.text import slugify

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


def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(1000_000, 25_500_000)
        slug = f"{slug}-{rand_int}"
        slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance
