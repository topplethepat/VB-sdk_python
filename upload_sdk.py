#LA Dec 2017
#this script will POST an audio file and return its status and mediaID

import time
import voicebase_client
from voicebase_client import *
from voicebase_client.rest import ApiException
from pprint import pprint
import json
# Configure API key authorization: Authorization
voicebase_client.configuration.api_key['Authorization'] = 'eyJ'
# create an instance of the API class
voicebase_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
mediaApi = voicebase_client.MediaApi()
client = voicebase_client.ApiClient()
media = 'PCI_stereo_henry.mp3'
response = mediaApi.post_media(media=media)
pprint (response)