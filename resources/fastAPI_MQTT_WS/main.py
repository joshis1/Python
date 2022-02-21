from fastapi import FastAPI
from fastapi_mqtt import FastMQTT, MQTTConfig
from pydantic import BaseModel
from ipaddress import IPv4Address
import jsonpickle

app = FastAPI()


class Nmap(BaseModel):
    host: IPv4Address
    portRange: str

    class Config:
        schema_extra = {
            "example" : {
                "host": "10.0.2.15",
                 "portRange": "22-80",
                 "description": "Scan the port from 22 to 80 of the ip address 10.0.2.15"
            }
        }



mqtt_config = MQTTConfig()

mqtt = FastMQTT(config=mqtt_config)

mqtt.init_app(app)

@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe("/mqtt/toModel/#") # subscribing mqtt topic wildcard- multi-level
    print("connected: ", client, flags, rc, properties)

@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("received message: ", topic, jsonpickle.decode(payload.decode()), qos, properties)
    return 0 


@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)

@app.get("/")
async def func():
    mqtt.client.publish("/mqtt", "Hello from fastApi") 
    return {"result": True, "message": "Published"}

@app.post("/scan/{host}")
async def scan_host_port(nmap_details : Nmap):
    results = {"got_val" : nmap_details}
    print(type(nmap_details))
    mqtt.client.publish("/mqtt/fromModel/nmap", jsonpickle.encode(nmap_details)) 
    return results