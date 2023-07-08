# battery_module_testing

serial_to_csv.py is a serial monitoring application which also saves all the data to data.csv

sketch_a2d_daq_module_testing contains the sketch(firmware) for the A2D 64 Channel DAQ

<<<<<<< HEAD
if you want to change the firmware on the DAQ, refer to the following Arduino library: https://github.com/mbA2D/A2D_DAQ

## thermistors & the daq

1. thermistors provide resistance as a function of temperature:

[NTC 10K 3380s](https://octopart.com/nxrt15xh103fa1b030-murata-25915268)

2. the daq captures the voltage across the thermistor

[A2D 64CHDAQ Documentation](</module_testing_daq/A2D%2064CHDAQ%20Documentation%20(Draft).pdf>)

3. these values can then be interpolated to temperature values

\(\frac{V}{{3.3-V}} \cdot (3.3 \times 10^3)\)

4. # calibrating the thermistors
   if you want to change the firmware on the DAQ, refer to the README for the following Arduino library: https://github.com/mbA2D/A2D_DAQ
   > > > > > > > 785e357e4ab967e53bc71525a39d2616389ceea2
