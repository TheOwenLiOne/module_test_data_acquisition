import serial
import csv
import re

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
        print(line)  # Print the line to the console

        if i>=2:
            data = re.findall(r'(?<!\d)\d{3,}(?!\d)', line)
            time_step.extend(data)

            if len(time_step) >= 64:
                csvWriter.writerow(time_step[:64])
                time_step = time_step[64:]

        i+=1

    except KeyboardInterrupt:
        break

dataFile.close()
ser.close()
