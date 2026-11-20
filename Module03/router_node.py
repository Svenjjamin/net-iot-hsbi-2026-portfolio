import time
from umqtt.simple import MQTTClient

BROKER = "192.168.14.1"
POD = "pod10"

UPTIME_TOPIC = (POD + "/router/uptime").encode()
SET_TOPIC = (POD + "/router/set").encode()

def on_message(topic, payload):
    print("Command received on {}: {}".format(
        topic.decode(), payload.decode()
    ))

client = MQTTClient(
    client_id=(POD + "-router-node").encode(),
    server=BROKER,
    port=1883,
    keepalive=30,
)
client.set_callback(on_message)
client.connect()
client.subscribe(SET_TOPIC)

print("Connected to MQTT broker at {}:1883".format(BROKER))
print("Subscribed to {}".format(SET_TOPIC.decode()))

last_publish = time.ticks_ms()

while True:
    client.check_msg()

    now = time.ticks_ms()
    if time.ticks_diff(now, last_publish) >= 1000:
        uptime_seconds = time.ticks_ms() // 1000
        client.publish(UPTIME_TOPIC, str(uptime_seconds).encode())
        last_publish = now

    time.sleep_ms(100)