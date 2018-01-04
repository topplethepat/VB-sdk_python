# LA Dec 2017
# this script will PUT metadata

import time
import voicebase_client
from voicebase_client import *
from voicebase_client.rest import ApiException
from pprint import pprint
import json

# Configure API key authorization: Authorization
voicebase_client.configuration.api_key[
    'Authorization'] = 'eyJ'
voicebase_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
mediaApi = voicebase_client.MediaApi()
apiClient = ApiClient()
metadataPut = MediaApi()
fdata = {"metadata":{"extended": {"callInformation": "validQ1"}}}
metadataPut.set_metadata_by_id('1e8e7c4f-7ae6-4c4a-a8e8-505011a074cf', fdata)