from __future__ import annotations
from  dataclasses import dataclass, field

@dataclass
class MeasurementValues:
    '''Object for storing measurment data loaded from file.'''
    voltage: list[float]
    power: list[float]
    tempRadiator: list[float]
    tempBattery: list[float]
    capacity: list[float]
    time: list[float]


def parse_file(file):
    parseRows = file.split("\n")

    # allValues = []
    voltage = []
    power = []
    tempRadiator = []
    tempBattery = []
    capacity = []
    time = []
    for row in parseRows[:-1]:
        parseColumns = row.split("\t")
        napatie = parseColumns[1]
        vykon = parseColumns[3]
        teplotaChladica = parseColumns[5]
        teplotaBaterie = parseColumns[7]
        kapacita = parseColumns[9]
        cas = parseColumns[11]
        # allValues.append([napatie, vykon, teplotaChladica, teplotaBaterie, kapacita, cas])
        voltage.append(float(napatie))
        power.append(float(vykon))
        tempRadiator.append(float(teplotaChladica))
        tempBattery.append(float(teplotaBaterie))
        capacity.append(float(kapacita))
        time.append(float(cas))
    
    valueObject = MeasurementValues(voltage, power, tempRadiator, tempBattery, capacity, time)
    return valueObject