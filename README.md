# Serial
This project is divided into two parts:
        
        1. Reading data from the Load cell(measuring weight) by using Arduino after this it sends the data from the Load cell to the USB             port.
            For this, we require a specific library i.e HX711_ADC (if this is not present in your Arduino ide)
        2. Now, we read stream data from the serial(USB port) by the using Serial library of Python.


Suppose there is a Gas cylinder with an initial weight of 30 kg. During the usage of Gas, there is a decrease in the weight of the Gas cylinder continuously. We want to measure the amount of use of LPG gas after every 10 seconds. So that we can understand the pattern of using LPG gas and we can also figure out how much LPG gas is used at different times(breakfast, Lunch, Dinner) and also at what rate gases burn out at different times.


