import requests
import json
import sys

from datetime import date
from utilities.config import Config

class WebClient(object):
    base_url = "n/a"

    def __init__(self):
        self.base_url = Config().get_integration_api_base_url()

    def show_api_result_details(self, result):
        print (f"Result code: {result.status_code}")
        if result.status_code == 200:
            print (self.get_json_text(result.json()))
        print (result.headers)
        print ("==================================================================")
        print()

    def get_json_text(self, obj):
        # create a formatted string of the Python JSON object
        return json.dumps(obj, sort_keys=True, indent=4)

    def get_json_object(self, obj):
        # create a json object that can be traversed
        return json.loads(self.get_json_text(obj))

    def transform_sensor_data(self, sensor_list):
        # date.today()

        data = [
            {
                "name": "Water Level",
                "type": 1,
                "stringValue": "0",
                "readTime": "2021-03-13T20:03:29.605Z",
            }
        ]

        return data
    
    def upload_sensor_readings(self, sensor_data, node_id):
        url = f"{self.base_url}/node/UpdateNodeSensors/{node_id}"
        data = self.transform_sensor_data(sensor_data)

        username = Config().get_integration_api_username()
        password = Config().get_integration_api_password()

        success = False

        try:
            # TODO: Remove verify=False before deploying to production (Local Testing Only)
            print("Update sensors")
            requests.put(url, json=data, auth=(username, password), verify=False) 

            success = True
        except:
            e = sys.exc_info()[0]
            print(f"Failed to update sensor reading. Error details >> {e}")

        # finally:
             # client.show_result_details(response)

        return success