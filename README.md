# ESP32 Temperature and Humidity Sensor

## Setup
### connect DHT22

- connect `+` on DHT to `3v3` on ESP32  
- connect `-` on DHT to `GND` on ESP32  
- connect `OUT` on DHT to `D15` on ESP32 

### Flash micropython
First you have to flash micropython to the ESP32.  
Firmware can be found [here](https://micropython.org/download#esp32).  


1. If you havn't already install esptool: `pip install esptool`  
2. Now you first need to erase the flash of the ESP32: `esptool.py --port /dev/ttyUSB0 erase_flash`  
2.HINT: If you run into permission problems you may need to add your user to the `dialout`group (Linux), requires a relogin afterwards to take effect
3. Now you can flash micropython to the ESP32: `esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-<version-you-downloaded>.bin`

if you now connect via terminal to the ESP32 e.g. `picocom /dev/ttyUSB0 -b115200`, you will have python shell: `>>>`

### connect to WIFI
connect the ESP32 to your network using this snippet (`CTRL + E` allows pasting of multiple lines, use `CTRL + D` to fire):

```python
import network


def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    ssid = '<yourSSID>'
    pw = '<yourWIFIpassword'
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, pw)
        while not sta_if.isconnected():
            print("waiting for connection...")
    print('successfully connected to ', ssid)
    print('network config: ', sta_if.ifconfig())

connect_to_wifi()
```
### Configure WEBREPL
You will need WEBREPL to easily upload the python scripts to your ESP32.  
Just `import webrepl_setup` and follow the instructions.
Afterwards execute this snippet, just to be sure webrpl is running:
```python
import webrepl

webrepl.start()
```


### Upload python scriptsto the ESP32
Ok your ESP32 is connected to your WIFI and it printed you its IP address.
Download webrepl now to be able to connect to your ESP32.
```bash
git clone git@github.com:micropython/webrepl.git
```
If you don't have git configured you can also just download it [here](https://github.com/micropython/webrepl) as a zip.

- Ok now open `webrepl.html` from this repo.  
- On the top left replace the IP with the one of your ESP32 and click on `Connect`.
- You need to enter the password you entered when setting up WEBREPL before.  
- Once you are connected you use send file on the right to upload boot.py and main.py.  
- Remember to replace the placeholders in `boot.py` with your WIFI credentials and the id if your sensor in `main.py`

Now disconnect your ESP32 and reconnect it to power/your USB port.

If you now open the IP of your ESP32 in the browser it should return you a JSON object like this:
```json
{
    "humidity": 53.2,
    "id": "schlafzimmer",
    "temperature": 21.8
}
```





