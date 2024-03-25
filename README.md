# CIS600ASSIGMENT3

Using the previous iteration of a lab involving the ESP32 and micropython I added the functionality of generating random numbers for all fields using urandom library, this allows more variety of data. Now with the code finished, I set up a device on thingspeak, and I set up a channel with 3 fields corresponding to the values that are generated. I take the key information and write api keys to the code and put the new information in, and give the device publish and subscribe capabilities. Now this means my IOT device is ready to send data, and as you can see the graphs are generated each time the mqtt broker receives data.

The 3 included m files are matlab visualizations that thingspeak provides to visualize sensor data. This code makes it so that each sensor's data is visualized withing the 5 hour time period, and updates itself when new data is registered.
