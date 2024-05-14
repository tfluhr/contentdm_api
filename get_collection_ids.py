def get_collection_ids(x):
    collection_ids = []
    my_call = f'https://{x}/digital/bl/dmwebservices/index.php?q=dmGetCollectionList/json'

    response = requests.get(my_call)
    data = response.json()

    for i in data:
        collection_ids.append(i['secondary_alias'])

    return(collection_ids)
