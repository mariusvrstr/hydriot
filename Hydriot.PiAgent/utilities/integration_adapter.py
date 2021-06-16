import asyncio
from datetime import datetime
from adapters.hydriot_web_api import WebClient
from settings.app_config import AppConfig

class IntegrationAdapter(object):
    _frequency_in_seconds = 1    
    _is_monitoring = False
    _sensors = None
    _node_id = "n/a"
    last_integration_update = None
    previous_integration_success = False

    def __init__(self, update_frequency):
        self._frequency_in_seconds = update_frequency
        self._node_id = AppConfig().get_integration_node_id()
    
    async def register_integration(self):
        self._is_monitoring = True

        if self._sensors != None or self._node_id == "n/a":
            pass

        while self._is_monitoring:
            await asyncio.sleep(self._frequency_in_seconds)

            if not AppConfig().get_integration_enabled():                
                continue

            # Send updated sensor data
            client = WebClient()
            success = client.upload_sensor_readings(self._sensors, self._node_id)

            if success:
                self.previous_integration_success = True
                self.last_integration_update = datetime.now()
            else:
                self.previous_integration_success = False          
                          
        pass

    def stop_monitoring(self):
        self._is_monitoring = False

    def start_monitoring(self, sensors):
        self._sensors = sensors
        asyncio.ensure_future(self.register_integration())  
        pass
    
    def cleanup(self):
        self.stop_monitoring()
        pass
