# module testing | data acquisition

[serial_to_csv.py](serial_to_csv.py) is a serial monitoring application which also writes all the data to [data.csv](data.csv)

[sketch_a2d_daq_module_testing](sketch_a2d_daq_module_testing) contains the sketch(arduino firmware) for the A2D 64 Channel DAQ

if you want to change the firmware on the DAQ, refer to the following Arduino library: https://github.com/kostubhagarwal/A2D_DAQ

## thermistors & daq

Thermistors provide resistance as a function of temperature:
[NTC 10K 3380s](https://octopart.com/nxrt15xh103fa1b030-murata-25915268)

1. the daq measures the voltage across a thermistor using a voltage divider configuration:
   [A2D 64CHDAQ Documentation](</module_testing_daq/documentation/A2D%2064CHDAQ%20Documentation%20(Draft).pdf>)

   ![](/documentation/image.png)

2. the voltage can be used to calculate the resistance of the thermistor
   [thermistor_calc.py](thermistor_calc.py)

   $V*{\text{{thermistor}}} = \frac{{V*{\text{{thermistor}}}}}{{V_{\text{{daq}}} - V*{\text{{thermistor}}}}} \cdot R*{\text{{daq}}}$

3. the temperature can be interpolated from the thermistor resistance:
   [thermistor_calc.py](thermistor_calc.py)

   $T = \frac{1}{{\frac{1}{{T_0}} + \frac{1}{B} \cdot \ln(R)}}$

4. calibrating the thermistors (TO-DO):
   [Thermistor calibration](https://www.mstarlabs.com/sensors/thermistor-calibration.html)
