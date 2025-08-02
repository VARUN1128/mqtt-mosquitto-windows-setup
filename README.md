
````markdown
# MQTT Mosquitto Windows Setup

This repository provides a simple guide to setting up an MQTT broker using [Mosquitto](https://mosquitto.org/) on a Windows system, with support for custom ports, WebSocket, and local testing.

---

## 🚀 Features

- Mosquitto 2.0+ on Windows
- Custom port configuration (1884)
- WebSocket support (9001)
- CLI testing with `mosquitto_pub` and `mosquitto_sub`
- Works locally for Python, Node.js, and IoT integration

---

## 🧰 Requirements

- Windows 10 or later
- Mosquitto (Download from: https://mosquitto.org/download/)

---

## 🔧 Configuration

### 1. mosquitto.conf

Example configuration:

```conf
listener 1884
protocol mqtt

listener 9001
protocol websockets

allow_anonymous true
````

📁 Save this as:
`C:\Program Files\mosquitto\mosquitto.conf`

---

## ▶️ Running the Broker

Open Command Prompt:

```bash
"C:\Program Files\mosquitto\mosquitto.exe" -c "C:\Program Files\mosquitto\mosquitto.conf" -v
```

---

## 🧪 Testing the Broker

### Publish a message:

```bash
mosquitto_pub -h localhost -p 1884 -t test/topic -m "Hello from Publisher"
```

### Subscribe to a topic:

```bash
mosquitto_sub -h localhost -p 1884 -t test/topic
```

You should see the published message on the subscriber side.

---

## 🐍 Example Python Client

```python
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("localhost", 1884)
client.subscribe("test/topic")
client.on_message = on_message
client.loop_forever()
```

---

## 🔐 Optional: Enable Password Authentication

```bash
mosquitto_passwd -c "C:\Program Files\mosquitto\pwfile.txt" your_username
```

Update config:

```conf
allow_anonymous false
password_file "C:\Program Files\mosquitto\pwfile.txt"
```

---

## 📂 Repository Structure

```
mqtt-mosquitto-windows-setup/
├── mosquitto.conf
├── README.md
```

---

## 🧠 Credits

* Mosquitto: [https://mosquitto.org/](https://mosquitto.org/)
* paho-mqtt Python client: [https://pypi.org/project/paho-mqtt/](https://pypi.org/project/paho-mqtt/)

---

## 📬 License

This project is MIT licensed.

```

---

Would you like me to generate this repo structure for you locally or push it to GitHub via command line instructions?
```
