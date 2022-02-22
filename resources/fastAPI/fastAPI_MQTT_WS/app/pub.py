import random
import time 

from paho.mqtt import client as mqtt_client


broker = '10.0.2.15'

port = 1883

topic = "house/t1"

client_id = "p1"


def connect_mqtt():
    def on_connect(client, userData, flags, rc):
        if rc == 0:
            print('connected to mqtt broker')
        else:
            print('failed to connect to broker')
    
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client 


def publish(client):
    msg_count = 0 
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)

        status = result[0]

        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()