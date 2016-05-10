__author__ = 'musunuru'
import threading
import time
import paho.mqtt.client as mqtt
import db_layer
from smartbathroom.settings import mqtt_host

topic = "ui"
publish_topic = "sensor_control"
db = db_layer.db_layer("noti")

janitor_msg = "Hi, Service needed for wash room %s"
user_msg = "Hi, Washroom %s is empty now."

def on_connect(client, userdata, flags, rc):
    print("[MQTT]Connected with result code "+str(rc))
    client.subscribe(topic,0)

def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))
    data = {}
    if msg.topic == topic:
        data = eval(msg.payload)
        print data
        id = data["restroom_id"]
        if str(data["service"]) == "1":
            janitor_list = db.get_data({"restroom_id":str(id), "type" :"service"})
            for i in janitor_list:
                send_text(i["telno"],janitor_msg %(id))
                db.remove({"_id":i["_id"]})

        for i in data["door"]:
            if str(i["status"]) == "1":
                user_list = db.get_data({"restroom_id":str(id), "type" :"room"})
                print user_list
                for j in user_list:
                    send_text(j["telno"],user_msg %(i["id"]))
                    db.remove({"_id":j["_id"]})




def send_text(number,msg):
    print number+" "+msg

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_host, 1883, 60)

def mqtt_function():
    client.loop_forever()

def start_mqtt_listener():
    t = threading.Thread(name='mqtt_thread', target=mqtt_function)
    t.start()