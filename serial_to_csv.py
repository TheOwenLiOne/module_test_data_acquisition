import serial
import csv
import thermistor_calc as tc


def initialize_csv_file(filename, columns):
    """
    Create a .csv with 64 columns(one for each channel).
    """
    with open(filename, 'w', newline='') as data_file:
        csv_writer = csv.writer(data_file)
        header = [str(i) for i in range(columns)]
        csv_writer.writerow(header)


def read_serial_data(ser):
    """
    Extract and convert serial data to 'utf-8' strings.
    """
    try:
        return ser.readline().decode('utf-8').strip()
    except ValueError:
        return None


def formatting_serial(line):
    """
    Extract voltage from a 'utf-8' string.
    """
    try: 
        return float(line.split()[2]) / 1000
    except ValueError:
        return None


def main():

    i = 0
    b = 2
    columns = 64
    step = []
    state = True

    # Configuring serial communication and initializing CSV file
    ser = serial.Serial('COM3', 115200) #initialize COM5 port with 115200 Baud
    file_name = 'data.csv'
    initialize_csv_file(file_name, columns)

    #User I/O
    choice = input("Enter 1 to start program or enter 2 to end program: ")
    print("Program started. Press Ctrl+C to pause the program.")

    #Main progam loop
    while state:
        if choice == "1":
            try:
                line = read_serial_data(ser)

                # Skipping first two columns of serial data
                if i >= 2:
                    voltage = formatting_serial(line)
                    temperature = round(tc.calculate_temperature(tc.calculate_resistance(abs(voltage))), 2)
                    step.append(temperature)

                    # Live monitoring
                    if temperature > -40:
                        channel = b - 2
                        print(f"Channel {channel}: {temperature}")

                    # Writing data to .csv
                    if len(step) >= 64:
                        with open(file_name, 'a', newline='') as data_file:
                            csv_writer = csv.writer(data_file)
                            csv_writer.writerow(step[:64])
                            step = step[64:]

                    if i % 64 == 0:
                        b = 0
                        print(f"---------------------------------------------------")
                    b += 1
                i += 1

            except KeyboardInterrupt:
                choice = input("Enter 1 to continue program or 2 to end program: ")

        elif choice == "2":
            print("Program ended. Data is stored in 'data.csv'.")
            state = False

        else:
            print("Invalid entry. Please enter 1 or 2")
            choice = input("Enter 1 to start program or enter 2 to end program: ")
            print("Program started. Press Ctrl+C to pause the program.")

    ser.close()


if __name__ == "__main__":
    main()
