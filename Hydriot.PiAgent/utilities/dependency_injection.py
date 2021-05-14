from dependency_injector import containers, providers
from utilities.app_config import AppConfig

from sensors.tds_sensor import TDSSensorStub, TDSSensor
from sensors.water_level_sensor import WaterLevelSensorStub, WaterLevelSensor
from sensors.ph_sensor import PhSensorStub, PhSensor
from sensors.light_sensor_infrared import LightSensorInfraredStub, LightSensorInfrared

from triggers.light_trigger import LightRelayStub, LightRelay
from triggers.pump_trigger import PumpRelayStub, PumpRelay

class Container(containers.DeclarativeContainer):
    simulate = AppConfig().get_enable_sim()

    tds_factory = providers.Factory(TDSSensorStub) if simulate else providers.Factory(TDSSensor)
    water_level_sensor_factory = providers.Factory(WaterLevelSensorStub) if simulate else providers.Factory(WaterLevelSensor)
    ph_sensor_factory = providers.Factory(PhSensorStub) if simulate else providers.Factory(PhSensor)
    light_sensor_infrared_factory = providers.Factory(LightSensorInfraredStub) if simulate else providers.Factory(LightSensorInfrared)
    
    light_relay_factory = providers.Factory(LightRelayStub) if simulate else providers.Factory(LightRelay)
    pump_relay_factory = providers.Factory(PumpRelayStub) if simulate else providers.Factory(PumpRelay)

    pass

