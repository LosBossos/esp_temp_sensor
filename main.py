import machine
import dht
import socket
import ujson

d = dht.DHT22(machine.Pin(15))
sensor_id = "<egRoomYourSensorIsPlacedIn>"
temp = None
hum = None

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    response = {"id": sensor_id,
                "temperature": temp,
                "humidity": hum}
    cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
    cl.send(ujson.dumps(response))
    cl.close()