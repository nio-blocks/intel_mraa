IntelMraaInterruptGpio
======================
Use Intel's libmraa to handle gpio interrupts from the IO on Galileo, Edison & other platforms.

Properties
----------
- **mraa_gpio_pin**: The Mraa pin number. For Edison, see pin number mappings [here](https://github.com/intel-iot-devkit/mraa/blob/master/docs/edison.md)

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: None.

Commands
--------
None

Dependencies
------------
mraa

IntelMraaReadGpio
=================
Use Intel's libmraa to read the IO on Galileo, Edison & other platforms. Reads are driven by input signals.

Properties
----------
- **mraa_gpio_pin**: The Mraa pin number. For Edison, see pin number mappings [here](https://github.com/intel-iot-devkit/mraa/blob/master/docs/edison.md)

Inputs
------
- **default**: Any list of signals. One read will be made per input signal.

Outputs
-------
- **default**: Each input signal is output with the added attribute `pin`, which is the value read from the specified pin.

Commands
--------
None

Dependencies
------------
mraa

IntelMraaWriteGpio
==================
Use Intel's libmraa to write to the IO on Galileo, Edison & other platforms.

Properties
----------
- **mraa_gpio_pin**: The Mraa pin number. For Edison, see pin number mappings [here](https://github.com/intel-iot-devkit/mraa/blob/master/docs/edison.md)
- **value**: The value to write to the specified **mraa_pin_#**. Regular boolean interpretation is done here except the string '0' is treated as `False`.

Inputs
------
- **default**: Any list of signals. One write will be made per a signal.

Outputs
-------
- **default**: Each input signal is output with the added attribute `write_status` which is the status value returned by the pin write.

Commands
--------
None

Dependencies
------------
mraa
