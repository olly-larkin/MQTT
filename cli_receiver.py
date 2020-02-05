import paho.mqtt.client as mqtt
import ssl

client = mqtt.Client()

# ee-estott-octo.ee.ic.ac.uk:1883
# test.mossquitto.org:1883

broker = 'ee-estott-octo.ee.ic.ac.uk'
port = 1883

client.connect(broker, port)
print('Connected')

def on_message(client, userdata, message):
    print("Received message: {}".format(message.payload))

client.on_message = on_message
client.subscribe('IC.embedded/LH/testing')

client.loop_forever()
