def pub(brokeradress,username,passwordd):
    import random
    import time
    import paho.mqtt.client as mqtt

    brokerAdress = f"{brokeradress}"
    userName = f"{username}"
    password = f"{passwordd}"

    topic = "Sensor/Temparature/TMP36"

    def on_connnect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected succesfully")
        else:
            print("Connected returned result code:", str(rc))

    def on_message(client, userdata, message):
        print("Received message:" + message.topic + "=>>" + message.payload.decode("utf-8"))

    client = mqtt.Client()
    client.on_connect = on_connnect
    client.on_message = on_message

    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    client.username_pw_set(userName, password)
    client.connect(brokerAdress, 8883)

    min = 10
    max = 100
    wait = 3
    while True:
        data = random.randint(min, max)
        client.publish(topic, data)
        print(data)
        time.sleep(wait)





