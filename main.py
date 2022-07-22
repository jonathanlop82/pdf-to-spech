import requests
import urllib3

from PyPDF2 import PdfReader

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://app.beyondwords.io/api/v4/projects/16557/audio"

#Delete audio

def del_audio(id):

    url = "https://app.beyondwords.io/api/v4/projects/16557/audio/"+id

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer write_dc74ae8b9ac2a12ec9d60ba1194b0f80"
    }

    response = requests.delete(url, headers=headers, verify=False)

    print(response.text)

#Read PDF

reader = PdfReader("document2.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

# Create audio

payload = {
    "body": f"{text}",
    "title": "speech"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer write_dc74ae8b9ac2a12ec9d60ba1194b0f80"
}

response = requests.post(url, json=payload, headers=headers, verify=False)

print(response.text)

#List audio

headers = {"Accept": "application/json","Authorization": "Bearer write_dc74ae8b9ac2a12ec9d60ba1194b0f80"}

response = requests.get(url, headers=headers, verify=False)

print(response.text)

data = response.json()
print(data)
# print(data[0]['media'][1]['url'])

# url_media = data[0]['media'][1]['url']
# response = requests.get(url_media, verify=False)
# open("speech.mp3", "wb").write(response.content)

# for media in data:
#     print(media)
#     media_id = media['id']
#     print(media_id)
#     del_audio(str(media_id))





