import mraa

from nio.properties import VersionProperty
from nio.block.base import Block

from .intel_mraa_gpio_base import IntelMraaGpioBase


class IntelMraaReadGpio(IntelMraaGpioBase, Block):

    """ Use Intel's libmraa to interface with the IO on various platforms """

    version = VersionProperty("1.0.0")

    def _pin_mode(self):
        return mraa.DIR_IN

    def _process_signal(self, signal):
        signal.pin = self._gpio_pin.read()
        return signal
