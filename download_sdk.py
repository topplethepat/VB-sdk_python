#LA Dec 2017
#this script will GET a json file using its mediaID

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
response = mediaApi.get_media_by_id_with_http_info('735f59be-df90-464c-82c7-044ac84c831f')
pprint(response)