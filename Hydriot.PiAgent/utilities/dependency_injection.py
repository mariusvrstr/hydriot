from dependency_injector import containers, providers
from utilities.config import Config

from sensors.tds_sensor import TDSSensorStub, TDSSensor
from sensors.water_level_sensor import WaterLevelSensorStub, WaterLevelSensor
from triggers.light_trigger import LightRelayStub, LightRelay

class Container(containers.DeclarativeContainer):
    simulate = Config().get_enable_sim()

    tds_factory = providers.Factory(TDSSensorStub) if simulate else providers.Factory(TDSSensor)
    water_level_sensor_factory = providers.Factory(WaterLevelSensorStub) if simulate else providers.Factory(WaterLevelSensor)
    light_relay_factory = providers.Factory(LightRelayStub) if simulate else providers.Factory(LightRelay)

    pass

