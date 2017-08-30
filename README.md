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
[**mraa**](https://github.com/intel-iot-devkit/mraa): This is not on PyPI and requires additional install steps. Follow the install instructions on [sparkfun](https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison) with a couple of updates:
- The step `apt-get install python-dev` needs to be updated to `apt-get install python3-dev`
- The step `cmake .. -DBUILDSWIGNODE=OFF` needs to be updated to `cmake .. -DBUILDSWIGNODE=OFF -DBUILDPYTHON3=ON`
- When appending the python path in `.bashrc` as outlined in the instructions, there is a syntax error: `export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))` should have double quotes inside it, like so: `export PYTHONPATH=$PYTHONPATH:$(dirname $"(find /usr/local -name mraa.py)")` If that doesn't work, then `export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.4/site-packages` should suffice.
- Optionally, create a symlink between the mraa files in `/usr/local/lib/python3.4/site-packages` and `/usr/local/lib/python3.4/dist-packages`, like so:
- `sudo ln -s /usr/local/lib/python3.4/site-packages/_mraa.so /usr/local/lib/python3.4/dist-packages/_mraa.so`
- `sudo ln -s /usr/local/lib/python3.4/site-packages/mraa.py /usr/local/lib/python3.4/dist-packages/mraa.py`
- If using **rc.local** to start n.io, GPIO will not be accessible. This is due to the fact that the above step has you append the python path in **.bashrc**, which is loaded after **rc.local**. Since this is the case, n.io has already initialized before it knows where the mraa library is. Fix this by appending the python path with the path to the `mraa.py` file & `_mraa.so` shared library in **rc.local**, rather than in **.bashrc**.


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
[**mraa**](https://github.com/intel-iot-devkit/mraa): This is not on PyPI and requires additional install steps. Follow the install instructions on [sparkfun](https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison) with a couple of updates:
- The step `apt-get install python-dev` needs to be updated to `apt-get install python3-dev`
- The step `cmake .. -DBUILDSWIGNODE=OFF` needs to be updated to `cmake .. -DBUILDSWIGNODE=OFF -DBUILDPYTHON3=ON`
- When appending the python path in `.bashrc` as outlined in the instructions, there is a syntax error: `export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))` should have double quotes inside it, like so: `export PYTHONPATH=$PYTHONPATH:$(dirname $"(find /usr/local -name mraa.py)")` If that doesn't work, then `export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.4/site-packages` should suffice.
- Optionally, create a symlink between the mraa files in `/usr/local/lib/python3.4/site-packages` and `/usr/local/lib/python3.4/dist-packages`, like so:
- `sudo ln -s /usr/local/lib/python3.4/site-packages/_mraa.so /usr/local/lib/python3.4/dist-packages/_mraa.so`
- `sudo ln -s /usr/local/lib/python3.4/site-packages/mraa.py /usr/local/lib/python3.4/dist-packages/mraa.py`
- If using **rc.local** to start n.io, GPIO will not be accessible. This is due to the fact that the above step has you append the python path in **.bashrc**, which is loaded after **rc.local**. Since this is the case, n.io has already initialized before it knows where the mraa library is. Fix this by appending the python path with the path to the `mraa.py` file & `_mraa.so` shared library in **rc.local**, rather than in **.bashrc**.
