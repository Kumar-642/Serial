# About the Project
This project is:
        
  1. Reading data from the Load cell(AtoD converter) by using Arduino after this it sends the data from the Load cell to the USB port.
       For this, we require a specific library i.e HX711_ADC (if this is not present in your Arduino ide, you can download and get more         about that from the 'HX711_ADC' folder)
  2. Now, we read stream data from the serial(USB port) by the using Serial library of Python.
  3. 'Final_data1.xlsx' is a small demo of reading at the interval of every 10 seconds from the 1000g of the water container.
     ( Due to hardware laxness ,there might be an error of +50 or -50)

# Description of Project
Suppose there is a Gas cylinder with an initial weight of 30 kg. During the usage of Gas, there is a decrease in the weight of the Gas cylinder continuously. We want to measure the amount of use of LPG gas after every 10 seconds. So that we can understand the pattern of using LPG gas and we can also figure out how much LPG gas is used at different times(breakfast, Lunch, Dinner) and also at what rate gases burn out at different times. Once we read the rate of consumption for 15 minutes(90 data points), we do further analysis like predicting the time to finish the 'x' amount of gas by the linear regression model. In future, we will proceed with our project to enhance the project reliability. We might do some better data analysis, so we will get some better results.
