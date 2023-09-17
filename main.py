import sys
from physical import *

if __name__ == "__main__":
    getPort()
    setDevice1(True)
    setDevice2(True)
    test_temp = readTemperature()                                                                                                                                                                                  
    test_mois = readMoisture()                                                                                                                                                                                     
    print('Temperature and Moisture value is:', test_temp, ' and ', test_mois)