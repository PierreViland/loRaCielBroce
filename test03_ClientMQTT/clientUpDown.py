import os
import sys
import logging
import paho.mqtt.client as mqtt
import json
import csv
import random
import datetime
import mysql.connector

USER = "_____________________"
PASSWORD = "__________________________________________________________________________________________________"
PUBLIC_TLS_ADDRESS = "___________________________"
PUBLIC_TLS_ADDRESS_PORT = 8883
DEVICE_ID = "____________________"
ALL_DEVICES = True

test= 0
# Meaning Quality of Service (QoS)
# QoS = 0 - at most once
# QoS = 1 - at least once
# QoS = 2 - exactly once


QOS = 0

#conn = mysql.connector.connect(host="___",
#                                  user="___",
#                                  password="___",
#                                  database="_____")

cursor = conn.cursor()



def stop(client):
    client.disconnect()
    print("\nFin")
    sys.exit(0)



#Fonction callback lorsque le client recoit en ACK du server
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("\nConnexion OK avec le MQTT broker")
    else:
        print("\nFErreur de connexion = " + str(rc))


#Fonction callback quand le server diffuse une info
def on_message(client, userdata, message):
    print("\nMessage recu de l'abonnement '" + message.topic + "' avec QoS = " + str(message.qos))

    global test
    test = json.loads(message.payload)
    parsed_json = json.loads(message.payload)
    print("Payload brut: ")
    print( json.dumps(parsed_json, indent=4))
    
    if "uplink_message" in parsed_json:
        temp_max     = parsed_json['uplink_message']['decoded_payload']['temperature_1']
        temp_min    = parsed_json['uplink_message']['decoded_payload']['temperature_2']
        id_gateway   = parsed_json['uplink_message']['rx_metadata'][0]['gateway_ids']['gateway_id']
        rssi         = parsed_json['uplink_message']['rx_metadata'][0]['rssi']
        timep = datetime.datetime.now() 
        
        prtin("Data Reçu.")
        print(temp_min)
        print(temp_max)
        print(id_gateway)
        print(rssi)
        print(timep)
    
        #sql = "INSERT INTO mesures_device1 (ID, ____, ___, _____, ___, ___) VALUES (NULL, %s, %s, %s, %s, %s)"
        #val = (str(____), str(____), str(____), str(____), str(____) )
        #cursor.execute(sql, val)
        #conn.commit()
    else :
        print("Pas de bonne donnees")
   
#Subsription a un abonndment MQTT.
def on_subscribe(client, userdata, mid, granted_qos):
    print("\nSouscription au abonnement " + str(mid) + " avec QoS = " + str(granted_qos))

#Deabonnement
def on_disconnect(client, userdata, rc):
    print("\nDeconnexion du broker = " + str(rc))

#Affichage log
def on_log(client, userdata, level, buf):
    print("\nLog: " + buf)
    logging_level = client.LOGGING_LEVEL[level]
    logging.log(logging_level, buf)


# Gene ID client
client_id = f'python-mqtt-{random.randint(0, 1000)}'

print("Create new mqtt client instance")
mqttc = mqtt.Client(client_id)

#Assignation des fonctions de rappel 'callback fct'
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message
mqttc.on_disconnect = on_disconnect
# mqttc.on_log = on_log  # Logging for debugging OK, waste


print("Configuration  broker: " + PUBLIC_TLS_ADDRESS + ":" + str(PUBLIC_TLS_ADDRESS_PORT))
mqttc.username_pw_set(USER, PASSWORD)
mqttc.tls_set()
mqttc.connect(PUBLIC_TLS_ADDRESS, PUBLIC_TLS_ADDRESS_PORT, 60)
mqttc.subscribe("#", QOS)


print("boucle infinie")
try:
    run = True
    while run:
        mqttc.loop(10)  # seconds timeout / blocking time
        print(".", end="", flush=True)  # Affichage d'info pour montrer que le programme est 'en vie'
        
        #A LIRE  POUR LE DOWNLINK
        #Exemple POUR ENVOYER UN MESSAGE au device
        #hexadecimal_payload = '016700AD026700A6030101'
        #fport = 3
        #b64 = b64encode(bytes.fromhex(hexadecimal_payload)).decode()
        #print('Convert hexadecimal_payload: ' + hexadecimal_payload + ' to base64: ' + b64)
        #msg = '{"downlinks":[{"f_port":' + str(fport) + ',"frm_payload":"' + b64 + '","priority": "NORMAL"}]}'
        #result = mqttc.publish(topic, msg, QOS)

        # result: [0, 2]
        #status = result[0]
        #if status == 0:
        #    print("Send " + msg + " to topic " + topic)
        #else:
        #    print("Failed to send message to topic " + topic)
        #FIN DOWNLINK
        
        
except KeyboardInterrupt:
    stop(mqttc)
