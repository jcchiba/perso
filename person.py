"""
The example returns a JSON response whose content is the same as that in
  ../resources/personality-v3-expect2.txt
"""
import json
from os.path import join, dirname
from ibm_watson import PersonalityInsightsV3
import csv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

# Authentication via IAM
authenticator = IAMAuthenticator('VGvpWN_mGFd73ZC2sViJ3BssUUYa8mSOq77qMUZjv_ZL')
service = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator)
service.set_service_url('https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/405c419a-0568-4416-89fb-fe3010dae61d')

# Authentication via external config like VCAP_SERVICES
#service = PersonalityInsightsV3(version='2017-10-13')
#service.set_service_url('https://gateway.watsonplatform.net/personality-insights/api')

############################
# Profile with JSON output #
############################

# with open(join('personality-v3.json')) as \
#         profile_json:
#     profile = service.profile(
#         profile_json.read(),
#         'application/json',
#         raw_scores=True,
#         consumption_preferences=True).get_result()
#
#     print(json.dumps(profile, indent=2))

###########################
# Profile with CSV output #
###########################

# with open(join('personality-v3.json'), 'r') as \
#         profile_json:
#     response = service.profile(
#         profile_json.read(),
#         accept='text/csv',
#         csv_headers=True).get_result()


with open('personality.txt', 'r') as profile_text:
        profile = service.profile(profile_text.read(), content_language='es', accept_language='en', accept='application/json').get_result()

print(json.dumps(profile, indent=2))

with open('personality.txt', 'r') as profile_text:
        profile = service.profile(profile_text.read(), content_language='es', accept_language='en', accept='text/csv',csv_headers=True).get_result()


profile = profile.content
cr = csv.reader(profile.decode('utf-8').splitlines())
my_list = list(cr)
for row in my_list:
     print(row)
