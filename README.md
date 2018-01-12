# Speedtest
#### Measures download speed, upload speed and ping saves offline and uploads data to Thingspeak

*Requires speedtest-cli to be installed: https://github.com/sivel/speedtest-cli*

Basic usage:

> python speedtest.py

Sends data in every 10 mins and saves data to .csv:

> crontab -e

> */10 * * * * /usr/bin/python /home/pi/speedtest/speedtest-cron.sh



*tamasharasztosi, 2018*
