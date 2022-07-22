import requests
from requests.structures import CaseInsensitiveDict

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://developer.voicemaker.in/voice/api"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer 29687310-088f-11ed-a79a-93b71d283abb"
headers["Content-Type"] = "application/json"

data = '{"Engine": "neural", "VoiceId": "ai3-Jony", "LanguageCode": "en-US", "Text": "Welcome to the Air.", "OutputFormat": "mp3", "SampleRate": "48000", "Effect": "default", "MasterSpeed": "0", "MasterVolume": "0", "MasterPitch": "0" }'


resp = requests.post(url, headers=headers, data=data, verify=False)

data = resp.json()

print(data)