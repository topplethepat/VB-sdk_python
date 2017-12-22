#LA Dec 2017
#This script will upload an audio file and includes a configuration for PCI redaction and speaker ID/stereo


import time
import voicebase_client
from voicebase_client import *
from voicebase_client.rest import ApiException
from pprint import pprint
import json
# Configure API key authorization: Authorization
voicebase_client.configuration.api_key['Authorization'] = 'eyJ'
# create an instance of the API class
# create an instance of the API class
voicebase_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
mediaApi = voicebase_client.MediaApi()
client = voicebase_client.ApiClient()
media = 'PCI_stereo_henry.mp3'
config = VbConfiguration(
  prediction = VbPredictionConfiguration(
    detectors = [ VbDetectorConfiguration(
         detector_name="PCI",
         redactor = VbRedactorConfiguration(
               transcript = VbTranscriptRedactorConfiguration(replacement="[redacted]") ) ) ]),
  ingest = VbIngestConfiguration(
    stereo= VbStereoConfiguration(
       left= VbChannelConfiguration(speaker_name="Jennifer"),
       right= VbChannelConfiguration(speaker_name="Pedro"))) )
response = mediaApi.post_media(media=media, configuration=config)
pprint (response)