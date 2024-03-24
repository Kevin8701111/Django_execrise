from meter.meter_action.getapi import apivalue

class Meter(object):
    def __init__(self, ip, model, phase) -> None:
        self.ip = ip
        self.model = model
        self.phase = phase

    def meter_address_value(self,address):
        if address == '0x1001':
            voltage = apivalue.fetch_voltage(address)
            return voltage
        elif address == '0x1008':
            amperage = apivalue.fetch_amperage(address)
            return amperage
        elif address == '0x1010':
            active_power = apivalue.fetch_active_power(address)
            return active_power
        elif address == '0x101D':
            frequency = apivalue.fetch_frequency(address)
            return frequency
        elif address == '0x101C':
            power_factor = apivalue.fetch_power_factor(address)
            return power_factor
        else:
            return 'no data'