import requests
import shutil

#  This function downloads object source files
#  Might be better to use GetFile API function below:
#  https://help.oclc.org/Metadata_Services/CONTENTdm/Advanced_website_customization/API_Reference/CONTENTdm_API/CONTENTdm_Website_API_Reference_utils


save_dir = "C:\\Users\\tfluhr\\Desktop\\dspace\\"
base_path = "https://cdm17133.contentdm.oclc.org/digital/api/singleitem/image/coll11/{}/default.jpg" # 410/default.jpg

item_dict = {
"sc17278":"410",
"sc17279":"411",
"sc17280":"412",
"sc17281":"413",
"sc17283":"414",
"sc17284":"415",
"sc17285":"416",
"sc17286":"417",
"sc17288":"418",
"sc17289":"419",
"sc17290":"420"
}

for i in item_dict:
    img_url = base_path.format(item_dict[i])
    print("dspace identifier: " + i + " - " + img_url)
    response = requests.get(img_url, stream=True)
    with open(save_dir + i + ".jpg", 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
