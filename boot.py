import network
import webrepl


def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    ssid = '<yourSSID>'
    pw = '<yourWIFIpassword>'
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, pw)
        while not sta_if.isconnected():
            print("waiting for connection...")
    print('successfully connected to ', ssid)
    print('network config: ', sta_if.ifconfig())

connect_to_wifi()
webrepl.start()
