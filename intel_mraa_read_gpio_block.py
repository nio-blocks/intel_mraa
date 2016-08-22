import mraa
from nio.signal.base import Signal
from nio.util.discovery import discoverable
from .intel_mraa_gpio_base import IntelMraaGpioBase


@discoverable
class IntelMraaReadGpio(IntelMraaGpioBase):

    """ Use Intel's libmraa to interface with the IO on various platforms """

    def _pin_mode(self):
        return mraa.DIR_IN

    def _process_signal(self, signal):
        signal.pin = self._gpio_pin.read()
        return signal
