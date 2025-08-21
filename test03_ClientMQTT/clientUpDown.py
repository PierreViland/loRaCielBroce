import os
import sys
import logging
import paho.mqtt.client as mqtt
import json
import datetime
import mysql.connector
import random

# --- Configuration ---
BROKER_ADDRESS = "192.1__________"  # MQTT non sécurisé sur port 1883
BROKER_PORT = 1883
QOS = 0  # Qualité de service

DEVICE_TOPIC = "application/ee1__________71f9/device/678________59c/event/up"


# Base de données MySQL
#conn = mysql.connector.connect(
#     host="192.________",
#     user="____",
#     password="_____",
#    database="_________"
#)
#cursor = conn.cursor()

# --- Fonctions utilitaires ---
def stop(client):
    client.disconnect()
    print("\nFin")
    sys.exit(0)

# --- Callbacks adaptés Paho 2.x ---
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("\nConnexion OK avec le MQTT broker")
    else:
        print("\nErreur de connexion = " + str(rc))

def on_message(client, userdata, message):
    print(f"\nMessage reçu du topic '{message.topic}' avec QoS={message.qos}")
    try:
        parsed_json = json.loads(message.payload)
        print("Payload brut:\n", json.dumps(parsed_json, indent=4))
        
        if "object" in parsed_json:
            temp_max = parsed_json['object']['temperatureSensor'].get('1')
            temp_min = parsed_json['object']['temperatureSensor'].get('2')

            # rxInfo est une liste, on prend le premier élément
            first_rx = parsed_json['rxInfo'][0]  # [0] pour accéder au premier dictionnaire
            id_gateway = first_rx.get('gatewayId')
            rssi = first_rx.get('rssi')
            


            timep = datetime.datetime.now()
            id_device = parsed_json['deviceInfo'].get('devEui')
            print(f"Temp min: {temp_min}, Temp max: {temp_max}")
            print(f"Temp min: {temp_min}, Temp max: {temp_max}")
            print(f"Id device: {id_device}")
            #sql = "INSERT INTO Mesure (id_mesure, temp_min, ____________________________________"

            # val = (str(________), ___________________________________)
            #cursor.execute(sql, val)
            #conn.commit()
        else:
            print("Pas de bonnes données")
    except Exception as e:
        print("Erreur traitement message:", e)

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print(f"\nSouscription au topic {mid} avec QoS={granted_qos}")

def on_disconnect(client, userdata, rc, properties=None):
    print(f"\nDéconnexion du broker, rc={rc}")

# --- Création du client ---
client_id = f'python-mqtt-{random.randint(0,1000)}'
mqttc = mqtt.Client(client_id=client_id)

# Assignation des callbacks
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe
mqttc.on_disconnect = on_disconnect

# Connexion au broker non sécurisé
mqttc.connect(BROKER_ADDRESS, BROKER_PORT, 60)
mqttc.subscribe(DEVICE_TOPIC, QOS)

# --- Boucle principale ---
print("Boucle infinie MQTT...")
try:
    while True:
        mqttc.loop(10)  # Timeout 10s
        print(".", end="", flush=True)
except KeyboardInterrupt:
    stop(mqttc)
