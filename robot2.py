import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    x, y = msg.payload.decode().split(",")
    print(f"Received robot1 location: X={x}, Y={y}")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("robot1/location")
client.on_message = on_message

client.loop_forever()
