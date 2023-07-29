import math

# Thermistor parameters
R0 = 10000  # Reference resistance in ohms
T0 = 298.15  # Reference temperature in Kelvin (25 degrees Celsius)
B = 3380  # Beta value
X = 273.15  # Convert from Kelvin to Celsius

# Daq parameters
V_daq = 3.3 # Daq voltage in volts
R_daq = 3.3e3 # Daq resistance in ohms

def calculate_resistance(V):
    try:
        R = V / (V_daq - V) * R_daq
        return R
    except ZeroDivisionError:
        return None

def calculate_temperature(R):
    if R >= 0:
        try:
            ln_R_R0 = math.log(R / R0)
            inv_T = (1 / T0) + (1 / B) * ln_R_R0
            T = 1 / inv_T
            T -= X
            return T
        except ZeroDivisionError:
            return None