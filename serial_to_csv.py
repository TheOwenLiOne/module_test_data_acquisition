import serial
import csv
import thermistor_calc as tc

dataFile = open('data.csv', 'w', newline='') # create csv file
csvWriter = csv.writer(dataFile) # create csv writer object
header = [str(i) for i in range(64)] # initiate columns for csv file
csvWriter.writerow(header) # write header to csv file

ser = serial.Serial('COM5', 115200)  # set the serial port to COM5, baud rate 115200

i = 0 # counter for number of lines read
b = 2 # counter for channels
step = [] #initial list of reading for a given time
state = True #state variable

choice = input("Enter 1 to start program or enter 2 to end program: ")
print("Program started. Press Ctrl+C to pause")

while state:
    if choice == "1":
        try:
            line = ser.readline().decode('utf-8').strip()  # Read a line of serial data
            if i>=2:
                v = (float(line.split()[2]))/1000 # extract voltage from serial monitor (V)
                temperature = tc.calculate_temperature(tc.calculate_resistance(abs(v))) # calculate temperature from voltage across thermistor (C)
                step.append(temperature) # append temperature to list of readings for a given time
                if temperature > -40:  
                    a = b - 2     
                    print(temperature, a)
                if len(step) >= 64:
                    csvWriter.writerow(step[:64]) # write 64 readings to csv file
                    step = step[64:]
                if i%64==0:
                    b = 0
                b+=1
            i+=1
            
        except KeyboardInterrupt:
            choice = input("Enter 1 to Continue, 2 to End: ")

    elif choice == "2":
        print("Program ended.")
        state = False

    else:
        print("Invalid choice. Please enter 1 or 2")

dataFile.close()
ser.close()