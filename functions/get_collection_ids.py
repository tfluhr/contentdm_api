import requests
import json

#  This just finds collection IDS for ContentDM instance
#  API Documentation here:
#  https://help.oclc.org/Metadata_Services/CONTENTdm/Advanced_website_customization/API_Reference/CONTENTdm_API/CONTENTdm_Server_API_Functions_dmwebservices
#  Define some things

contentdm_url = "cdm17133.contentdm.oclc.org"

def get_collection_ids(x):
    collection_ids = []
    my_call = f'https://{x}/digital/bl/dmwebservices/index.php?q=dmGetCollectionList/json'

    response = requests.get(my_call)
    data = response.json()

    for i in data:
        collection_ids.append(i['secondary_alias'])

    return(collection_ids)

ids = get_collection_ids(contentdm_url)

print("collection ids:" ,ids)
