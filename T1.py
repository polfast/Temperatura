import os
import csv
from time import sleep
from datetime import date, time, datetime

#get GPU temp from Rpi
def gpu_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return temp.replace("temp=", "")

#get CPU temp from Rpi
def cpu_temp():
    temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    return temp.replace("temp=", "")

# Change "Temp.csv" to rename file for output data
# "sleep(60) change to choice how often data should be writed to file
while True:
    with open('Temp.csv', 'a', encoding='utf-8', newline='') as tempfile:
        csvwriter = csv.writer(tempfile, delimiter=',')
        CPU = int(cpu_temp()) / 1000
        dzien = date.today()
        now = datetime.now()
        godzina = now.strftime("%H:%M:%S")
        csvwriter.writerow([dzien, godzina, 'CPU temp', int(CPU), 'GPU temp', gpu_temp()])
        sleep(60)
