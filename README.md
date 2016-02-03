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
   -   When appending the python path in .bashrc as outlined in the instructions, there is a syntax error: `export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))` should have double quotes inside it, like so: `export PYTHONPATH=$PYTHONPATH:$(dirname $"(find /usr/local -name mraa.py)")` If that doesn't work, then `export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.4/site-packages` should suffice.
   -   If using **rc.local** to start n.io, GPIO will not be accessible. This is due to the fact that the above step has you append the python path in **.bashrc**, which is loaded after **rc.local**. Since this is the case, n.io has already initialized before it knows where the mraa library is. There are two potential fixes for this:
   -   *Either*:
          -   Append the python path with the path to the `mraa.py` file & `_mraa.so` shared library in **rc.local**, rather than in **.bashrc**.   *--or--*
          -   Move the `mraa.py` file and `_mraa.so` library to a directory that python is already aware of, such as: `/usr/local/lib/python3.4/dist-packages`. To find a directory already in `$PYTHONPATH`, open the python interpreter (type `python3.4` and hit return) and enter: `import requests; requests.__file__` 


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
