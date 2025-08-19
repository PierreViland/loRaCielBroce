#####################################################
## Liste des librairies utilisées
######################################################
from machine import Timer
from machine import I2C
# configure the I2C bus
import pycom
from network import LoRa
import socket
import time
import ubinascii
from machine import UART
import machine
import math

#####################################################
## PENSER A LIRE LES COMMENTAIRES
######################################################

##Init variables
periodeHorloge = 10
tempMax = -100
tempMin = 100
address = 24
temp_reg = 5
res_reg = 8
dataAvailable = 0

######################################################
## Initi du capteur de temperature
######################################################
###############Init temperature
i2c = I2C(0, I2C.MASTER, baudrate=100000)
i2c.scan() # returns list of slave addresses
def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp

##################################Fin

######################################################
## Creation d'un objet timer
######################################################
class Clock:
    #Constructeur
    def __init__(self):
        #Init timer
        self.num_paquet = 0
        #self.__alarm = Timer.Alarm(Fct a executer toute, temps entre chaque execution , periodic ou Non)
        self.__alarm = Timer.Alarm(self._seconds_handler, periodeHorloge, periodic=True)

    #Fonction a exectuer a chaque tic du timer
    def _seconds_handler(self, alarm):
        global tempMax
        global tempMin
        print("Max : " + str(tempMax))  
        print("Min : " + str(tempMin))     
        tempMax = -100
        tempMin = 100

        #Possibilite d'arreter le timer
        #if self.seconds == 100:
        #    alarm.cancel() # stop counting after 10 seconds

######################################################
## Fin timer
######################################################



######################################################
## Debut Programme
######################################################

#Creation du Timer
clock = Clock()


while 1 : 
    data = i2c.readfrom_mem(address, temp_reg, 2)
    tempCurrent = temp_c(data)
    
    if tempCurrent > tempMax : 
        tempMax = tempCurrent
    if tempCurrent < tempMin : 
        tempMin = tempCurrent
   
#####################################################
## FIN
######################################################


