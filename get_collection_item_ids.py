import requests
import json
import math

def get_collection_info(x,y,z):
    my_call = f'https://{x}/digital/bl/dmwebservices/index.php?q=dmQuery/{y}/0/0/0/1/{z}/format/json'
    response = requests.get(my_call)
    data = response.json()
    return data['pager']



def get_item_ids(x,y,z):
    col_info = get_collection_info(contentdm_url, col_id, start_rec)
    api_runs = (math.ceil(col_info['total']/1024))

    dict = {
        'collection': col_id,
        'item_pointers': []
    }

    count = 0
    while count == 0:
        my_call = f'https://{x}/digital/bl/dmwebservices/index.php?q=dmQuery/{y}/0/0/0/1024/{z}/format/json'
        response = requests.get(my_call)
        data = response.json()
        for i in data['records']:
            dict['item_pointers'].append(i['pointer'])
        count += 1
        #print(count)
        #print(dict)
    while count < api_runs:
        my_call = f'https://{x}/digital/bl/dmwebservices/index.php?q=dmQuery/{y}/0/0/0/1024/{z + (count * 1024)}/format/json'
        response = requests.get(my_call)
        data = response.json()
        for i in data['records']:
            dict['item_pointers'].append(i['pointer'])
        count += 1
        #print(count)
        #print(dict)
    return(dict)
