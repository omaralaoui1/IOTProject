# subscriber
import paho.mqtt.client as mqtt
from Store_MQTT_Data_in_Database import sensor_Data_Handler
from datetime import datetime
import json
MQTT_Broker = "192.168.1.107"
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = "test/sensor"

#Subscribe
def on_connect(client, userdata, flags, rc):
	print("==Connected to Broker ==")
	client.subscribe(MQTT_Topic,0)

def on_message(mosq, obj, msg):
	print(msg.payload.decode())
	print(data_formated(msg.payload.decode()))


def data_formated(msg):
	SensorId = msg.split('#')[1]
	Temp = msg.split('TC/')[1].split('&')[0]
	Humidity = msg.split('TC/')[1].split('&')[1]
	Soil_Moisture = msg.split('TC/')[1].split('&')[2]

	Sensor_Data = {}
	Sensor_Data['Sensor_ID'] = SensorId
	Sensor_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
	Sensor_Data['Temperature'] = Temp
	Sensor_Data['Humidity'] = Humidity
	Sensor_Data['Soil_Moisture'] = Soil_Moisture
	return json.dumps(Sensor_Data)

def on_subscribe(mosq,obj,mid,granted_qos):
	pass

client = mqtt.Client()
#Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe= on_subscribe

#Connect
client.connect(MQTT_Broker,int(MQTT_Port), int(Keep_Alive_Interval))
client.loop_forever()

#  #3#TC/23.00&50.00&27
# 3 numéro de la zone
#23 température en °C
# 50.00 humidité %
# 27 humidité de sol %