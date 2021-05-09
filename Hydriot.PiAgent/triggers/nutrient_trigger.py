from triggers.contracts.dose_relay_abstract import DoseRelayAbstract
import time

# TODO: Add Light Schedule

class NutrientTrigger(DoseRelayAbstract):
        def __init__(self):
        DoseRelayAbstract.__init__(self)