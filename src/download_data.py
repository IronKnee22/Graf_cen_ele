import requests
import zipfile
import io

for i in range(2010, 2025):
    url = f"https://www.ote-cr.cz/pubweb/attachments/62_162/{i}/Rocni_zprava_o_trhu_{i}_V0.zip"
    print(url)


    response = requests.get(url)
    if response.status_code == 200:
        print("ZIP file download")
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall("data/raw")
            print("Success")
    else:
        print(f"Error while downloading file {response.status_code}")
