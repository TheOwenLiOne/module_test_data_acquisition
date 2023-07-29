import serial
import csv
import thermistor_calc as tc

ser = serial.Serial('COM3', 115200)  # set the serial port to COM3, baud rate 115200

dataFile = open('data.csv', 'w', newline='') # create csv file
csvWriter = csv.writer(dataFile) # create csv writer object
header = [str(i) for i in range(64)] # initiate columns for csv file
csvWriter.writerow(header) # write header to csv file

i = 0 # counter for number of lines read
time_step = [] #initial list of reading for a given time

while True:
    try:
        line = ser.readline().decode('utf-8').strip()  # Read a line of serial data

        if i>=2:
            v = (float(line.split()[2]))/1000 # extract voltage from serial monitor (V)
            temperature = tc.calculate_temperature(tc.calculate_resistance(abs(v))) # calculate temperature from voltage across thermistor (C)
            time_step.append(temperature) # append temperature to list of readings for a given time
            
            if len(time_step) >= 64:
                csvWriter.writerow(time_step[:64]) # write 64 readings to csv file
                time_step = time_step[64:]
        i+=1

    except KeyboardInterrupt:
        break

dataFile.close()
ser.close()