import mraa
from nio.signal.base import Signal
from nio.util.discovery import discoverable
from nio.properties import Property
from .intel_mraa_gpio_base import IntelMraaGpioBase


@discoverable
class IntelMraaWriteGpio(IntelMraaGpioBase):

    """ Use Intel's libmraa to interface with the IO on various platforms """

    value = Property(title='Pin Value', default='{{ $value }}')

    def _pin_mode(self):
        return mraa.DIR_OUT

    def _process_signal(self, signal):
        write_value = self._get_write_value(signal)
        signal.write_status = self._gpio_pin.write(write_value)
        return signal

    def _get_write_value(self, signal):
        value = self.value(signal)
        # if value is a string (Ex. '1'), see if it can be converted to an
        # int that will have a more meaningful value (Ex. 1 => True).
        if isinstance(value, str):
            try:
                value = int(value)
                value = bool(value)
            except:
                pass
        return value
