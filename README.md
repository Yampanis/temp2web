"# temp2web" 

Read temperature data from a USB Sensor connected to the CSC Clubhouse Ubuntu PC.  Uses installed Digitemp software to read and format the data.

https://www.digitemp.com/

The script temp2web.py runs command line arguments

1. Removes old temperature data file (temp2web.txt), reads the USB temperature probe, writes the formatted results to the data file.
2. copies the data file to a webserver


Troubleshooting:

# Check that digitemp can access the USB Temperature Sensor:

admin@csc-clubhouse:/home/cscone$ sudo digitemp -w -s/dev/ttyUSB1
[sudo] password for admin: 
DigiTemp v3.7.1 Copyright 1996-2015 by Brian C. Lane
GNU General Public License v2.0 - http://www.digitemp.com
Turning off all DS2409 Couplers
.
Devices on the Main LAN
28FF641E387D88E1 : DS18B20 Temperature Sensor

admin@csc-clubhouse:/home/cscone$ date
Mon Jul 17 11:30:39 PDT 2023
admin@csc-clubhouse:/home/cscone$

# Verify the OS can detect the USB Temperature Sensor (This output shows two sensors, each plugged into a separate USB Port Prolific Technonlgy nad QinHeng Electronics)

admin@csc-clubhouse:/home/cscone$ lsusb

Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 008 Device 002: ID 05b8:3280 Agiler, Inc. 
Bus 008 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 007 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 006 Device 002: ID 04f9:0035 Brother Industries, Ltd 
Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 007: ID 10c4:ea60 Cygnal Integrated Products, Inc. CP210x UART Bridge / myAVR mySmartUSB light
Bus 001 Device 002: ID 1a40:0101 Terminus Technology Inc. Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 004 Device 003: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port
Bus 004 Device 002: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 003 Device 002: ID 413c:2105 Dell Computer Corp. Model L100 Keyboard
Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
admin@csc-clubhouse:/home/cscone$ date
Mon Jul 17 11:32:45 PDT 2023
admin@csc-clubhouse:/home/cscone$ 
