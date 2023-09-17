print("Sensors and Actuators")
import time
import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort

portName = getPort()
try:
    ser = serial.Serial(port="/dev/ttyAMA2", baudrate=9600)
    print("Open COM successfully")
except:
    print('Can not open the port')
    

relay1_ON = [1,6,0,0,0,255,200,91]                                                                                                                                                                                 
relay1_OFF = [1,6,0,0,0,0,137,202]                                                                                                                                                                                 
                                                                                                                                                                                                                   
relay2_ON = [2,6,0,0,0,255,201,185]                                                                                                                                                                                
relay2_OFF = [2,6,0,0,0,0,137,249]                                                                                                                                                                                 
                                                                                                                                                                                                                   
relay3_ON = [3,6,0,0,0,255,200,104]                                                                                                                                                                                
relay3_OFF = [3,6,0,0,0,0,136,40]                                                                                                                                                                                  
                                                                                                                                                                                                                   
relay4_ON = [4,6,0,0,0,255,201,223]                                                                                                                                                                                
relay4_OFF = [4,6,0,0,0,0,137,159]                                                                                                                                                                                 
                                                                                                                                                                                                                   
relay5_ON = [5,6,0,0,0,255,200,14]                                                                                                                                                                                 
relay5_OFF = [5,6,0,0,0,0,136,38]                                                                                                                                                                                  
                                                                                                                                                                                                                   
relay6_ON = [6,6,0,0,0,255,200,61]                                                                                                                                                                                 
relay6_OFF = [6,6,0,0,0,0,136,125] 

def setDevice1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)

def setDevice2(state):
    if state == True:
        ser.write(relay2_ON)
    else:
        ser.write(relay2_OFF)
def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0
soil_temperature =[1, 3, 0, 6, 0, 1, 100, 11]
def readTemperature():
    serial_read_data(ser)
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
def readMoisture():
    serial_read_data(ser)
    ser.write(soil_moisture)
    time.sleep(1)
    return serial_read_data(ser)

ser.write(relay1_ON) 
print(serial_read_data(relay1_ON))                                                                                                                                                                                              
time.sleep(2)                                                                                                                                                                                                      
ser.write(relay1_OFF)             
print(serial_read_data(relay1_OFF))                                                                                                                                                                                  
time.sleep(2)                                                                                                                                                                                                      
print("Xong relay1")
                                                                                                                                                                                                                   
ser.write(relay2_ON)                                                                                                                                                                                               
time.sleep(2)                                                                                                                                                                                                      
ser.write(relay2_OFF)                                                                                                                                                                                              
time.sleep(2)   
                                                                                                                                                                                                  
print("Xong relay2")
                                                                                                                                                                                                                   
ser.write(relay3_ON)                                                                                                                                                                                               
time.sleep(2)                                                                                                                                                                                                      
ser.write(relay3_OFF)                                                                                                                                                                                              
time.sleep(2)                                                                                                                                                                                                      
print("Xong relay3")
                                                                                                                                                                                                                   
ser.write(relay4_ON)                                                                                                                                                                                               
time.sleep(2)                                                                                                                                                                                                      
ser.write(relay4_OFF)                                                                                                                                                                                              
time.sleep(2)                                                                                                                                                                                                      
print("Xong relay4")
                                                                                                                                                                                                                   
ser.write(relay5_ON)                                                                                                                                                                                               
time.sleep(2)                                                                                                                                                                                                      
ser.write(relay5_OFF)                                                                                                                                                                                              
time.sleep(2)                                                                                                                                                                                                      
print("Xong relay5")
                                                                                                                                                                                                                   
ser.write(relay6_ON)                                                                                                                                                                                               
time.sleep(2)                                                                                                                                                                                                      
ser.write(relay6_OFF)                                                                                                                                                                                              
time.sleep(2)                                                                                                                                                                                                      
print("Xong relay6")

while True:
    print("TEST SENSOR")
    print(readMoisture())
    time.sleep(1)
    print(readTemperature())
    time.sleep(1)