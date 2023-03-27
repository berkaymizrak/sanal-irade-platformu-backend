import json


# read json file and get object
def get_object_from_json_file(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


all_data = get_object_from_json_file('cities.json')

city_id = 0
town_id = 0
district_id = 0
prev_city = ''
prev_town = ''
for elem in all_data:
    if elem['city'] != prev_city:
        city_id += 1
    elem['city'] = {
        'id': city_id,
        'name': elem['city']
    }
    if elem['city']['name'] != prev_city or elem['town'] != prev_town:
        town_id += 1
    elem['town'] = {
        'id': town_id,
        'name': elem['town']
    }
    district_id += 1
    elem['district'] = {
        'id': district_id,
        'name': elem['district']
    }

    prev_city = elem['city']['name']
    prev_town = elem['town']['name']

json.dump(all_data, open('cities_raw_data.json', 'w'), indent=4)
