# Example : Let we have a water container of 1000gm and water flows out continously. We want to find the average amount of use of water 
#           in 5 sec and want to predict the total amount time required to empty whole container.So, here we take only 100 reading.

# This is small example but we can use same pricipal for large application by changing some parameter


import serial     # Importing Serial Library (this library does not work on Google collab)

# importing necessary library

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

print('Remove any weight before starting')    # Please empty your Load cell 
time.sleep(5)                                  # Wait to 5 seconds for empty 
ser = serial.Serial(port='/dev/cu.usbmodem11301',baudrate=57600)   # port name might be different for your system
print('Intialising setup please wait....')
time.sleep(1)
print('Put the weight on machine')    # Put the weight on Load cell 
timer = 11                            # Time gap of 11 seconds so that you can put weight on Load cell
for i in range(11):
    time.sleep(1)
    timer-=1
    print('waiting:',timer)
weights = []
i = 0
data_points = int(input('Enter Number of Data Points'))  # for this example we need only 100 data points
while i<data_points+1:
    # time.sleep(5)      # after every 5 seconds, it read weight of container
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
