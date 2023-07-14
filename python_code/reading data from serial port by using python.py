import serial

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
print('Remove any weight before starting')
time.sleep(5)
ser = serial.Serial(port='/dev/cu.usbmodem11301',baudrate=57600)
print('Intialising setup please wait....')
time.sleep(1)
print('Put the weight on machine')
timer = 11
for i in range(11):
    time.sleep(1)
    timer-=1
    print('waiting:',timer)
weights = []
i = 0
data_points = int(input('Enter Number of Data Points'))
while i<data_points+1:
    # time.sleep(10)
    ser = serial.Serial(port='/dev/cu.usbmodem1301',baudrate=57600)
    value=ser.readline()
    value = str(value,'UTF-8')
    # data = value[22:-2]
    data = value
    weights.append(data[:-2])
    time.sleep(10)
    print('done')
    i+=1
print(weights)
weights = weights[1:]
Sequence =range(1,data_points+1)
ser.close()
df = pd.DataFrame({'Sequence':Sequence,'Current weights':weights})
print(df)
df.to_excel('Final_test.xlsx')   # Data get saved in Excel file.
