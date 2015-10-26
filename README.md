IntelMraaGpioRead
=================

Use Intel's libmraa to read the IO on Galileo, Edison & other platforms

Reads are driven by input signals.

Properties
----------
-   **Mraa Pin #** (int): The Mraa pin number. For Edison, see pin number mappings [here](https://github.com/intel-iot-devkit/mraa/blob/master/docs/edison.md)

Dependencies
------------
-   [**mraa**](https://github.com/intel-iot-devkit/mraa): This is not on PyPI and require additonal install steps. Follow the install instruction on [sparkfun](https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison) with a couple updates:
   -   The step `apt-get install python-dev` needs to be updated to `apt-get install python3-dev`
   -   The step `cmake .. -DBUILDSWIGNODE=OFF` needs to be updated to `cmake .. -DBUILDSWIGNODE=OFF -DBUILDPYTHON3=ON`
   -   If `export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))` doesn't work then `export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.4/site-packages` should suffice`

Commands
--------
None

Input
-----
Any list of signals. One read will be made per input signal.

Output
------
Each input signal is output with the added attribute **pin** which is the value read from the specified pin.

--------------------------------------

IntelMraaGpioWrite
==================

Use Intel's libmraa to write to the IO on Galileo, Edison & other platforms

Properties
----------
-   **Mraa Pin #** (int): The Mraa pin number. For Edison, see pin number mappings [here](https://github.com/intel-iot-devkit/mraa/blob/master/docs/edison.md)
-   **Pin Value** (exp): The value to write to the specifed **Mraa Pin #**. Regular boolean interpretation is done here except the string '0' is treated as False.

Dependencies
------------
-   [**mraa**](https://github.com/intel-iot-devkit/mraa): This is not on PyPI and require additonal install steps. Follow the install instruction on [sparkfun](https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison) with a couple updates:
   -   The step `apt-get install python-dev` needs to be updated to `apt-get install python3-dev`
   -   The step `cmake .. -DBUILDSWIGNODE=OFF` needs to be updated to `cmake .. -DBUILDSWIGNODE=OFF DBUILDPYTHON3=ON`
   -   If `export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))` doesn't work then `export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.4/site-packages` should suffice`

Commands
--------
None

Input
-----
Any list of signals. One write will be made per a signal.

Output
------
Each input signal is output with the added attribute **write_status** which is the status value returned by the pin write.
