from beebotte import * 
import time
from random import randint


_hostname   = 'api.beebotte.com'

### Alternatively you can authenticate using the channel token
_token = '1472996037795_W8u5cuhbXfyb2euL'
bbt = BBT(token = _token, hostname = _hostname)
i = 0
zfz = 0



def getCpuTemperature():  
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )  
    cpu_temp = tempFile.read()  
    tempFile.close() 
    return float(cpu_temp)/1000



while True:
   
    bbt.write("Wetter", "Temp", getCpuTemperature())

    print (getCpuTemperature())
    
    
    time.sleep(20)
