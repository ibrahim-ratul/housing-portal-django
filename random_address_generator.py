import random_address
import random

number_of_addresses_required = 9
state_list = ['CT', 'CA', 'MA', 'VT', 'AL', 'AR', 'DC',
              'FL', 'GA', 'KY', 'MD', 'OK', 'TN', 'TX', 'AK', 'AZ']

for i in range(number_of_addresses_required):
    address_object = random_address.real_random_address_by_state(
        state_list[random.randint(0, len(state_list)-1)])

    adrs = address_object['address1'] or address_object['address2']
    city = address_object['city']
    postal_code = address_object['postalCode']
    state = address_object['state']

    address_string = f"{adrs}, {city}-{postal_code}, {state}"

    print(address_string)
