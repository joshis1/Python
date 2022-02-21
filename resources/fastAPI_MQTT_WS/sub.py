from paho.mqtt import client as mqtt_client
import jsonpickle
import nmap

broker = '10.0.2.15'
port = 1883

topic = "/mqtt/fromModel/nmap" 

client_id = "nmap"


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userData, flags, rc):
        if rc == 0:
            print("connected to mqtt broker")
        else:
            print('Failed to connec')

    client = mqtt_client.Client(client_id)
    client.connect(broker, port)
    return client 


def subscribe(client: mqtt_client):
    def on_message(client,userData, msg):
        print(f"Received  `{jsonpickle.decode(msg.payload.decode())}` from `{msg.topic}` topic")
        result = []
        nmap_info_received = jsonpickle.decode(msg.payload.decode())
        print(nmap_info_received.host)
        print(nmap_info_received.portRange)
        nm = nmap.PortScanner()
        nm.scan(format(nmap_info_received.host), nmap_info_received.portRange)
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                lport = sorted(lport)
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                    result.append({'port' : port, 'state' :  nm[host][proto][port]['state'] })
        print('Finished')
        print(result)
        client.publish("/mqtt/toModel/nmt", jsonpickle.encode(result))


    client.subscribe(topic)
    client.on_message = on_message



def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()



if __name__  == '__main__':
    run()