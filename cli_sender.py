import paho.mqtt.client as mqtt
import json
import datetime
from numpy import random

# ee-estott-octo.ee.ic.ac.uk:1883
# test.mosquitto.org:1883

broker = 'ee-estott-octo.ee.ic.ac.uk'
port = 1883

id = 1234

def getLight():
    return random.random()

def getTemp():
    return random.random()

def getHumidity():
    return random.random()

def payload():
    currentTime = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    return json.dumps({'id':id, 'timeStamp':currentTime, 'light':getLight(), 'temp':getTemp(), 'humidity':getHumidity()})

client = mqtt.Client()
client.connect(broker, port)
print('Connected')

while True:
    input('Press enter to send package...')
    client.publish('IC.embedded/LH/testing', payload())

