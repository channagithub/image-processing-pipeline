import zipfile
with zipfile.ZipFile("image_data/imgs_de.zip","r") as zip_ref:
    zip_ref.extractall(".")

