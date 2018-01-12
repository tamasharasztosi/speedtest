import os
import re
import subprocess
import time
import urllib2

response = subprocess.Popen('speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()

download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)
ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)

download[0] = download[0].replace(',', '.')
upload[0] = upload[0].replace(',', '.')
ping[0] = ping[0].replace(',', '.')

try:
    if os.stat('/home/pi/scripts/speedtest/speedtest.csv').st_size == 0:    # offline save to .csv
        print 'Date,Time,Download (Mbit/s),Upload (Mbit/s),Ping (ms)'
except:
    pass

print '{},{},{},{},{}'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), download[0], upload[0], ping[0])

myAPI = "FILL_WITH_YOUR_API"

baseURL = 'https://api.thingspeak.com/update?api_key=FILL_WITH_YOUR_API'
urllib2.urlopen(baseURL + "&field1=%s&field2=%s&field3=%s" % (download[0], upload[0], ping[0]))
