from collections import defaultdict
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from unittest import skipUnless
from unittest.mock import MagicMock, patch


mraa_available = True
try:
    from ..intel_mraa_read_gpio_block import IntelMraaReadGpio
except:
    mraa_available = False

@skipUnless(mraa_available, 'mraa is not available!!')
class TestIntelMraaReadGpio(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        # This will keep a list of signals notified for each output
        self.last_notified = defaultdict(list)

    def signals_notified(self, signals, output_id='default'):
        self.last_notified[output_id].extend(signals)

    def test_pass(self):
        pass
    
    @patch('mraa.Gpio')
    def test_defaults(self, mock_mraa_gpio):
        blk = IntelMraaReadGpio()
        self.configure_block(blk, {})
        blk.start()
        blk._gpio_pin.read = MagicMock(return_value = 1)
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(self.last_notified['default'][0].to_dict(), {"pin": 1})
