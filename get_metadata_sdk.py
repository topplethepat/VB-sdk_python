#LA Dec 2017
#this script will GET metadata from an uploaded file with media ID specified

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
#client = voicebase_client.ApiClient()
response = mediaApi.get_metadata_by_id('1e8e7c4f-7ae6-4c4a-a8e8-505011a074cf')

pprint(response)