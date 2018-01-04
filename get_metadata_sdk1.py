#LA Dec 2017
#this script will GET metadata from an uploaded file with media ID specified

import time
import voicebase_client
from voicebase_client import *
from voicebase_client.rest import ApiException
from pprint import pprint
import json

# Configure API key authorization: Authorization
voicebase_client.configuration.api_key['Authorization'] = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzOTY4ZTYyMC0xMGJkLTQ1OGYtYmJlYi0xMzcxMjVmYzNhYTMiLCJ1c2VySWQiOiJhdXRoMHw1ODUxYmNjNjUzYzI0YTA3M2MzYmNjNjciLCJvcmdhbml6YXRpb25JZCI6IjBiYTdkYjNmLTcyNDYtN2E2NS01NGQ2LTE5YTBkYTE3MDZlZSIsImVwaGVtZXJhbCI6ZmFsc2UsImlhdCI6MTQ4MjE2OTMzOTQ1MiwiaXNzIjoiaHR0cDovL3d3dy52b2ljZWJhc2UuY29tIn0.zlxLu8tZNTpzM0hcboVxZ99FrEgA5BoT35rT5T5tQbY'
# create an instance of the API class
voicebase_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
mediaApi = voicebase_client.MediaApi()
#client = voicebase_client.ApiClient()
response = mediaApi.get_metadata_by_id('735f59be-df90-464c-82c7-044ac84c831f')

pprint(response)