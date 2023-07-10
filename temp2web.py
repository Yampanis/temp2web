#!/usr/bin/env python
import os
import datetime
import time



timeStamp = str( int(time.time()) )

cmd = 'rm /home/admin/temp2web/temp2web.txt; digitemp -a -o "Sensor %s|%C|Celsius|' +timeStamp+ '\nSensor %s|%F|Fahrenheit|"' + timeStamp +' -c /home/admin/temp2web/.digitemprc  -l /home/admin/temp2web/temp2web.txt'
os.system(cmd)

cmd2 = 'curl -F "temp=@/home/admin/temp2web/temp2web.txt" -v https://whatskraken.cal-sailing.org/cam'
os.system(cmd2)

cmd3 = 'scp /home/admin/temp2web/temp2web.txt  konlanbi@konlanbi.com:~/public_html/csc/data/ '
os.system(cmd3)
