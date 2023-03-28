import json


def get_object_from_json_file(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


all_data = get_object_from_json_file('cities_raw_data.json')
codes = get_object_from_json_file('plakalar.json')

created_import_data = []

cities = []
towns = []
for elem in all_data:
    if elem['city']['id'] not in cities:
        code = next((code_elem['plaka_kodu'] for code_elem in codes if code_elem['il_adi'] == elem['city']['name']), '')
        cities.append(elem['city']['id'])
        created_import_data.append({
            'model': 'tools.city',
            'pk': elem['city']['id'],
            'fields': {
                'is_deleted': False,
                'updated_date': '2023-03-27T10:00:00.000Z',
                'created_date': '2023-03-27T10:00:00.000Z',
                'code': code
            }
        })
        created_import_data.append({
            'model': 'tools.citytranslation',
            'pk': elem['city']['id'],
            'fields': {
                'language_code': 'tr',
                'name': elem['city']['name'],
                'master': elem['city']['id']
            }
        })
    if elem['town']['id'] not in towns:
        towns.append(elem['town']['id'])
        created_import_data.append({
            'model': 'tools.town',
            'pk': elem['town']['id'],
            'fields': {
                'is_deleted': False,
                'updated_date': '2023-03-27T10:00:00.000Z',
                'created_date': '2023-03-27T10:00:00.000Z',
                'city': elem['city']['id']
            }
        })
        created_import_data.append({
            'model': 'tools.towntranslation',
            'pk': elem['town']['id'],
            'fields': {
                'language_code': 'tr',
                'name': elem['town']['name'],
                'master': elem['town']['id']
            }
        })
    created_import_data.append({
        'model': 'tools.district',
        'pk': elem['district']['id'],
        'fields': {
            'is_deleted': False,
            'updated_date': '2023-03-27T10:00:00.000Z',
            'created_date': '2023-03-27T10:00:00.000Z',
            'postal_code': '',
            'town': elem['town']['id']
        }
    })
    created_import_data.append({
        'model': 'tools.districttranslation',
        'pk': elem['district']['id'],
        'fields': {
            'language_code': 'tr',
            'name': elem['district']['name'],
            'master': elem['district']['id']
        }
    })

json.dump(created_import_data, open('cities_fixture.json', 'w'), indent=4)
