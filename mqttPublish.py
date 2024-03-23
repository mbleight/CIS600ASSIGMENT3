#Temp and Humidity data through ESP32 to ThingSpeak
#Use MQTT as publish/subsribe model

from machine import Pin, Timer
import network # module for network drivers and routing configuration
import ujson # module for Json data
import time # module for current time and date
import sys # Module that provides access to system-specific parameters and functions.
from umqtt.simple import MQTTClient # Built-in library for MQTT Protocol
from dht import DHT22
import urandom  # Import the urandom module for random number generation


#ThingSpeak MQTT Server Parameters
mqtt_client_id = "OCAQKiEgHygVLzwfNCIKNQA"
mqtt_user     = "OCAQKiEgHygVLzwfNCIKNQA"
mqtt_password  = "n7/7HcH6IHr4y25FvvsVx5nW"

mqtt_server = "mqtt3.thingspeak.com"


dht22 = DHT22(Pin(12)) # GPIO Pin 12 (DHT22 object created at Pin 12)
led = Pin(27, Pin.OUT)   # GPIO Pin 27 as an output

# ThinkSpeak Credentials
channel_ID = "2479227"
API_Key = "XPLJJSL2CHR0BU18"#"QPPICAQDJV70NRXB"

# Connect with WiFi
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

# Function to connect to local WiFi

def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.disconnect()
    wifi.connect(WIFI_SSID,WIFI_PASSWORD)
    if not wifi.isconnected():
        print('connecting to wifi..')
        timeout = 0
        while (not wifi.isconnected() and timeout < 10):
            print(10 - timeout)
            timeout = timeout + 1
            time.sleep(1) 
    if(wifi.isconnected()):
        print('connected to wifi')
    else:
        print('not connected to wifi')
        sys.exit()
    print('network config:', wifi.ifconfig())
        
connect_wifi() # Connecting to WiFi Router 

# Connection to MQTT Server
#create the MQTT client object
client = MQTTClient(client_id = mqtt_client_id, server =mqtt_server, user=mqtt_user, password=mqtt_password)
client.connect()
print("connected to MQTT server")

#create MQTT "Topic" to publish
publish_topic = b"channels/2479227/publish"
while True:
    time.sleep(5) 
    co2 = urandom.randint(300, 2000)
    hum = urandom.randint(0, 100)
    temp = urandom.randint(-50, 50)
    print("measuring temperature, humidity, and CO2")
    #dht22.measure()
    print("Temperature: {}".format(temp))
    print("Humidity: {}".format(hum))
    print("CO2: {}".format(co2))


#publishing data 
    message = "field1=" + str(temp) + "&field2=" + str(hum) + "&field3=" + str(co2)
    client.publish(publish_topic, message.encode("utf-8"))
    time.sleep(4)                      # Wait for 1 second

    print(" Msg sent to Thingspeak channel successfully...") 
    time.sleep(1)
