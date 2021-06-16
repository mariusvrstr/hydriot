from dependency_injector import containers, providers
from settings.app_config import AppConfig

from sensors.tds_sensor import TDSSensorStub, TDSSensor
from sensors.water_level_sensor import WaterLevelSensorStub, WaterLevelSensor
from sensors.ph_sensor import PhSensorStub, PhSensor
from sensors.light_sensor_infrared import LightSensorInfraredStub, LightSensorInfrared
from sensors.voltage_tester import VoltageTesterStub, VoltageTester

from triggers.nutrient_dispenser_trigger import NutrientDispenserRelayStub, NutrientDispenserRelay
from triggers.ph_down_trigger import PhDownRelayStub, PhDownRelay
from triggers.water_pump_trigger import WaterPumpRelayStub, WaterPumpRelay

class Container(containers.DeclarativeContainer):
    simulate = AppConfig().get_enable_sim()

    tds_factory = providers.Factory(TDSSensorStub) if simulate else providers.Factory(TDSSensor)
    water_level_sensor_factory = providers.Factory(WaterLevelSensorStub) if simulate else providers.Factory(WaterLevelSensor)
    ph_sensor_factory = providers.Factory(PhSensorStub) if simulate else providers.Factory(PhSensor)
    voltage_tester_factory = providers.Factory(VoltageTesterStub) if simulate else providers.Factory(VoltageTester)
    light_sensor_infrared_factory = providers.Factory(LightSensorInfraredStub) if simulate else providers.Factory(LightSensorInfrared)
    
    nutrient_relay_factory = providers.Factory(NutrientDispenserRelayStub) if simulate else providers.Factory(NutrientDispenserRelay)
    water_pump_relay_factory = providers.Factory(WaterPumpRelayStub) if simulate else providers.Factory(WaterPumpRelay)
    ph_down_relay_factory = providers.Factory(PhDownRelayStub) if simulate else providers.Factory(PhDownRelay)

    pass

