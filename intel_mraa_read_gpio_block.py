import mraa
from nio.common.signal.base import Signal
from nio.common.discovery import Discoverable, DiscoverableType
from .intel_mraa_gpio_base import IntelMraaGpioBase


@Discoverable(DiscoverableType.block)
class IntelMraaReadGpio(IntelMraaGpioBase):

    """ Use Intel's libmraa to interface with the IO on various platforms """

    def _pin_mode(self):
        return mraa.DIR_IN

    def _process_signal(self, signal):
        signal.pin = self._gpio_pin.read()
        return signal
