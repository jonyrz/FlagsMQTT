import paho.mqtt.client as mqtt

host = "192.168.40.1"
ncliente = "rod3"
topico = "msj"

def on_message(client, userdata, message):
    print("Mensaje Recibido " ,str(message.payload.decode("utf-8")))
    print("Mensaje Topico=",message.topic)
    print("Mensaje qos=",message.qos)
    print("Mensaje retain flag = ",message.retain)

#1. Crear un cliente con badnera clea_session = True
cliente = mqtt.Client(ncliente,clean_session = True)

#2. Asociar implementación ```on_message``` callback al cliente.
cliente.on_message = on_message

#3. Conectar el cliente al broker
cliente.connect(host)

print("Para recibir mensaje, primero hay que suscribirse")
cliente.subscribe(topico,qos= 0)

cliente.publish(topico,payload = "prueba3",retain = False, qos = 0)

#iniciar loop
cliente.loop_start()

cliente.loop_stop()
cliente.disconnect()
