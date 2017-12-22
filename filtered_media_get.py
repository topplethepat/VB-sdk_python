#LA Dec 2017
#this script will GET a transcript from an uploaded file without mediaID specified
#it can filter with use of keyword arguments, with the generic one here as (**{'query': 'query'})

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

response = mediaApi.media_query(**{'query':'query'})
pprint (response)