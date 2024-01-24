import serial
import csv
import thermistor_calc as tc

ser = serial.Serial('COM5', 115200)  # set the serial port to COM5, baud rate 115200

dataFile = open('data.csv', 'w', newline='')  # create csv file
csvWriter = csv.writer(dataFile)  # create csv writer object
header = [str(i) for i in range(64)]  # initiate columns for csv file
csvWriter.writerow(header)  # write header to csv file

i = 0  # counter for the number of lines read
time_step = []  # initial list of readings for a given time
paused = False  # flag to determine whether the loop is paused

while True:
    try:
        if not paused:
            line = ser.readline().decode('utf-8').strip()  # Read a line of serial data

            # Thermistor validation

            # Start Test

            # Pause Test
            if i >= 2:
                v = (float(line.split()[2])) / 1000  # extract voltage from the serial monitor (V)
                print("HELOO")

                temperature = tc.calculate_temperature(tc.calculate_resistance(abs(v)))  # calculate temperature from voltage across the thermistor (C)
                time_step.append(temperature)  # append temperature to the list of readings for a given time

                if temperature > -40:
                    a = i - 2
                    print(temperature, a)

                if len(time_step) >= 64:
                    csvWriter.writerow(time_step[:64])  # write 64 readings to the csv file
                    time_step = time_step[64:]

                if i == 64:
                    i = 0

                i += 1

        else:
            print("Paused. Press 'p' to resume or 'q' to quit.")
            user_input = input()

            if user_input.lower() == 'p':
                paused = False
            elif user_input.lower() == 'q':
                break

    except KeyboardInterrupt:
        break

dataFile.close()
ser.close()
