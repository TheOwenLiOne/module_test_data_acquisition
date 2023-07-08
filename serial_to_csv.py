import serial
import csv
import re
import thermistor_calc as tc

ser = serial.Serial('COM3', 115200)  
header = [str(i) for i in range(64)]
dataFile = open('data.csv', 'w', newline='')
csvWriter = csv.writer(dataFile)
csvWriter.writerow(header)

i = 0
time_step = []

while True:
    try:
        line = ser.readline().decode('utf-8').strip()  # Read a line of serial data

        if i>=2:
            v = float(line.split()[2])
            v /= 1000
            temperature = tc.calculate_temperature(tc.calculate_resistance(2.1))
            time_step.append(temperature)

            if len(time_step) >= 64:
                csvWriter.writerow(time_step[:64])
                time_step = time_step[64:]
        i+=1

    except KeyboardInterrupt:
        break

dataFile.close()
ser.close()