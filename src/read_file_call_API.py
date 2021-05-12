import json
import requests
from time import sleep
from ..conf import mongo_url, gg_api_key

Google_Places_API_key = gg_api_key

with open('read input.csv', 'r') as f:
    lines = f.readlines()  # .split('\n')
    # lines = lines

for line in lines:
    sleep(3)
    PLACES_API_URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&fields=name,place_id&input={}&key={}'.format(
        line.strip(), Google_Places_API_key)
    # print(PLACES_API_URL)
    print("Checking for:", line)
    try:
        PLACES_API_RESPONSE = requests.get(PLACES_API_URL)
        PLACES_API_DATA = PLACES_API_RESPONSE.json()
        # entity_name = PLACES_API_DATA['candidates'][0]['name']
        # place_id = PLACES_API_DATA['candidates'][0]['place_id']

        # print("entity_name: ",entity_name, "place_id: ",place_id)

        # FW

        with open("responses.csv", 'a') as f:
            f.write("{}\n".format(PLACES_API_DATA))

    except IndexError:
        print("0 results for ", line)

    except Exception as e:
        print("Exception has occoured in Places API call : {}".format(e))
