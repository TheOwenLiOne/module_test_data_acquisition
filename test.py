import serial
import csv
import thermistor_calc as tc


def initialize_csv_file(filename='data.csv', columns=64):
    with open(filename, 'w', newline='') as data_file:
        csv_writer = csv.writer(data_file)
        header = [str(i) for i in range(columns)]
        csv_writer.writerow(header)


def read_serial_data(ser):
    try:
        return ser.readline().decode('utf-8').strip()
    except ValueError:
        return None


def formatting_serial(line):
    return float(line.split()[2]) / 1000


def main():
    ser = serial.Serial('COM5', 115200)
    file_name = 'data.csv'
    initialize_csv_file(file_name)

    i = 0
    b = 2
    step = []
    state = True

    choice = input("Enter 1 to start program or enter 2 to end program: ")
    print("Program started. Press Ctrl+C to pause")

    while state:
        if choice == "1":
            try:
                line = read_serial_data(ser)
                if i >= 2:
                    voltage = formatting_serial(line)
                    temperature = tc.calculate_temperature(tc.calculate_resistance(abs(voltage)))
                    step.append(temperature)

                    if temperature > -40:
                        channel = b - 2
                        print(temperature, channel)

                    if len(step) >= 64:
                        with open(file_name, 'a', newline='') as data_file:
                            csv_writer = csv.writer(data_file)
                            csv_writer.writerow(step[:64])
                            step = step[64:]

                    if i % 64 == 0:
                        b = 0
                    b += 1
                i += 1

            except KeyboardInterrupt:
                choice = input("Enter 1 to Continue, 2 to End: ")

        elif choice == "2":
            print("Program ended.")
            state = False

        else:
            print("Invalid choice. Please enter 1 or 2")

    ser.close()


if __name__ == "__main__":
    main()
