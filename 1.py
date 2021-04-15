from Store_MQTT_Data_in_Database import sensor_Data_Handler
from datetime import datetime
import json
msg="#3#TC/23.00&50.00&27"

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




json_data = data_formated(msg)
print(json_data)
