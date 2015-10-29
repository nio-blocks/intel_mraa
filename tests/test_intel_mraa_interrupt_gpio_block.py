from collections import defaultdict
from nio.common.signal.base import Signal
from nio.util.support.block_test_case import NIOBlockTestCase
#from unittest import skipUnless
#from unittest.mock import MagicMock, patch
from ..intel_mraa_interrupt_gpio_block import IntelMraaInterruptGpio, interrupt_callback

class TestIntelMraaInterruptGpio(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        # This will keep a list of signals notified for each output
        self.last_notified = defaultdict(list)

    def signals_notified(self, signals, output_id='default'):
        self.last_notified[output_id].extend(signals)

    def test_pass(self):
        pass
    
    #@patch('mraa.Gpio')
    def test_defaults(self):
        blk = IntelMraaGpioInterrupt()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(0)
    
    #@patch('mraa.Gpio')
    def test_interrupt(self):
        blk = IntelMraaGpioInterrupt()
        self.configure_block(blk, {})
        blk.start()
        interrupt_callback(blk)
        #TODO: trigger callback somehow
        blk.stop()
        self.assert_num_signals_notified(1)
        [Signal()])
        self.assertDictEqual(self.last_notified['default'][0].to_dict(), {"pin_value": 0,
                        "pin_number": 10})
