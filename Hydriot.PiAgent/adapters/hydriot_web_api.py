import requests
import json
import sys
import time

from datetime import date
from settings.app_config import AppConfig
from utilities.console_manager import ConsoleManager

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
        data = []

        for key in sensor_list:
            sensor = sensor_list[key]
            data.append({
                "name": sensor._name,
                "type": 1,
                "stringValue": str(sensor.get_latest_value()),
                "readTime": sensor.get_last_read_time().strftime("%m/%d/%Y, %H:%M:%S")
            })         

        return data
    
    def upload_sensor_readings(self, sensor_data, node_id):
        url = f"{self.base_url}/node/UpdateNodeSensors/{node_id}"
        data = self.transform_sensor_data(sensor_data)

        username = AppConfig().get_integration_api_username()
        password = AppConfig().get_integration_api_password()

        success = False

        try:
            OperatingSystem().clear_console()
            print("Updating server over API...")

            # TODO: Remove verify=False before deploying to production (Local Testing Only)
            requests.put(url, json=data, auth=(username, password), timeout=8, verify=False)

            if response.status_code == 200:
                success = True

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            OperatingSystem().clear_console()
            print(f"Failed to update sensor readings. Error details >> {e}")
            # Sleep for 2s so that message is visible
            time.sleep(2)

            #raise SystemExit(e)           

        return success