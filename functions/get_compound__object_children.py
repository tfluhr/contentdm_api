import requests
import json

#  This function will find compound object parent's child obbjects
#  sample call for collections
#  https://cdm17133.contentdm.oclc.org/digital/bl/dmwebservices/index.php?q=dmGetCompoundObjectInfo/p17133coll6/41114/json
#  API Documentation here:
#  https://help.oclc.org/Metadata_Services/CONTENTdm/Advanced_website_customization/API_Reference/CONTENTdm_API/CONTENTdm_Server_API_Functions_dmwebservices


col_id = 'coll23'
contentdm_url = "cdm17133.contentdm.oclc.org"
cpds = [185, 343, 115, 326, 215, 39, 49, 303, 260, 59, 74, 340, 29, 280, 88, 152, 240] # removed 61 for now

cod = {
'collection': col_id,
'compound_objects': []
}

for i in cpds:
    cod['compound_objects'].append({"pointer" : i, "constituents" : []})


#print(cod)

#for i in cod['compound_objects']:
#   print(i['constituents'])


my_list = []
for x in cpds:
    my_call = f'https://{contentdm_url}/digital/bl/dmwebservices/index.php?q=dmGetCompoundObjectInfo/{col_id}/{x}/json'  #This is the call to get compound object constituents
    print(my_call)
    response = requests.get(my_call)
    data = response.json()
#    for i in (data['page']):
#        print(x )
    #    print(i['pageptr'])
    #    cpd_obj_collection_dictionary.update(i: i['pageptr'])
