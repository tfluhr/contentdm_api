import requests
import json
import math

#  This function finds compound object parents, and child objects in a collection
#  API Documentation here:
#  https://help.oclc.org/Metadata_Services/CONTENTdm/Advanced_website_customization/API_Reference/CONTENTdm_API/CONTENTdm_Server_API_Functions_dmwebservices
#  Define some things

contentdm_url = "cdm17133.contentdm.oclc.org"
col_id = 'coll23'
start_rec = 1

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
        'item_pointers': [],
        'cpds': []
    }

    count = 0
    while count == 0:
        my_call = f'https://{x}/digital/bl/dmwebservices/index.php?q=dmQuery/{y}/0/0/0/1024/{z}/format/json'
        response = requests.get(my_call)
        data = response.json()
        for i in data['records']:
            if i['filetype'] == 'cpd':
                dict['cpds'].append(i['pointer'])
            else:
                dict['item_pointers'].append(i['pointer'])
        count += 1
        #print(count)
        #print(dict)
    while count < api_runs:
        my_call = f'https://{x}/digital/bl/dmwebservices/index.php?q=dmQuery/{y}/0/0/0/1024/{z + (count * 1024)}/format/json'
        response = requests.get(my_call)
        data = response.json()
        for i in data['records']:
            if i['filetype'] == 'cpd':
                dict['cpds'].append(i['pointer'])
            else:
                dict['item_pointers'].append(i['pointer'])
        count += 1
        #print(count)
        #print(dict)
    return(dict)

collection_data = get_item_ids(contentdm_url, col_id, start_rec)
print("Compound Parents:", len(collection_data['cpds']), "Compound Children:" , len(collection_data['item_pointers']),)

print(collection_data)
