__author__ = 'musunuru'
import threading
import time
import paho.mqtt.client as mqtt
import db_layer
from smartbathroom.settings import mqtt_host

topic = "ui"
publish_topic = "sensor_control"
db = db_layer.db_layer("iot_data")
def on_connect(client, userdata, flags, rc):
    print("[MQTT]Connected with result code "+str(rc))
    client.subscribe(topic,0)

def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))
    data = {}
    if msg.topic == topic:
        data["data"] = eval(msg.payload)
        #print data
        db.set_realtime_data(data)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_host, 1883, 60)

def send_message(msg):
    client.publish(publish_topic, msg)

def mqtt_function():
    client.loop_forever()

def start_mqtt_listener():
    t = threading.Thread(name='mqtt_thread', target=mqtt_function)
    t.start()




