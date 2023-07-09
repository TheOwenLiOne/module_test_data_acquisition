# module testing | data acquisition

[serial_to_csv.py](serial_to_csv.py) is a serial monitoring application which also writes all the data to [data.csv](data.csv)

[sketch_a2d_daq_module_testing](sketch_a2d_daq_module_testing) contains the sketch(arduino firmware) for the A2D 64 Channel DAQ

## thermistors & daq

thermistors provide resistance as a function of temperature:
[NTC 10K 3380s](https://octopart.com/nxrt15xh103fa1b030-murata-25915268). the daq measures the voltage across a thermistor using a voltage divider configuration:
[A2D 64CHDAQ Hardware Documentation (by mbA2D)](</documentation/A2D_64CHDAQ_Hardware_Documentation_(Draft).pdf>)

![](/documentation/image.png)

the voltage can be used to calculate the resistance of the thermistor, from which temperature can be interpolated: [thermistor_calc.py](thermistor_calc.py)

$$R_{\text{{thermistor}}} = \frac{{V_{\text{{thermistor}}}}}{{V_{\text{{daq}}} - V_{\text{{thermistor}}}}} \cdot R_{\text{{daq}}}$$

$$T = \frac{1}{{\frac{1}{{T_0}} + \frac{1}{B} \cdot \ln(R_{\text{{thermistor}}})}}$$

## to-do

calibrate the thermistors: [thermistor calibration](https://www.mstarlabs.com/sensors/thermistor-calibration.html)

## acknowledgments

hardware, libraries, and documentation for the DAQ were created/designed by [mbA2D](https://github.com/mbA2D)
