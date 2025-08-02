import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    payload = f"{x},{y}"
    client.publish("robot1/location", payload)
    print(f"Published location: {payload}")
    time.sleep(2)
