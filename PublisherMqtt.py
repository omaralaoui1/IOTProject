
import paho.mqtt.client as paho
import sys

def onMessage(client, userdata, msg):
  print(msg.topic + ": " + msg.payload.decode())
  data_formated(msg.payload.decode)
  client.connect("192.168.1.107", 1883, 60)



client = paho.Client()
client.on_message = onMessage

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


if client.connect("192.168.1.107",1883,60) != 0 :
 print("Could not connect to MQTT Broker!")
 sys.exit(-1)

client.subscribe("test/status")

try:
 print("Press CTRL+C to exit...")
 client.loop_forever()
except:
  print("Disconnecting from  broker")

client.disconnect()