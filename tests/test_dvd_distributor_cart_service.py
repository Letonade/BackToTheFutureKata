import unittest
from application.dvd_distributor_cart_service import DvdDistributorCartService
from adapters.cli_adapter import CLIInputAdapter
from adapters.cli_adapter import CLIOutputAdapter
from core.dvd_distributor import DvdDistributor

class TestDvdDistributorService(unittest.TestCase):

    def setUp(self):
        self.dvd_distributor = DvdDistributor()
        self.input_adapter = CLIInputAdapter("")
        self.output_adapter = CLIOutputAdapter()
        self.service = DvdDistributorCartService(self.input_adapter, self.output_adapter, self.dvd_distributor)

    def test_empty_cart(self):
        self.input_adapter.set_cart("")
        total = self.service.handle_cart()
        self.assertEqual(total, 0.00)

    def test_single_dvd(self):
        self.input_adapter.set_cart("Back to the Future 1")
        total = self.service.handle_cart()
        self.assertEqual(total, 15.00)

    def test_two_different_dvds(self):
        self.input_adapter.set_cart("Back to the Future 1\nBack to the Future 3")
        total = self.service.handle_cart()
        self.assertEqual(total, 27.00)

    def test_three_different_dvds(self):
        self.input_adapter.set_cart("Back to the Future 1\nBack to the Future 2\nBack to the Future 3")
        total = self.service.handle_cart()
        self.assertEqual(total, 36.00)

    def test_four_dvds_with_one_duplicate(self):
        self.input_adapter.set_cart("Back to the Future 1\nBack to the Future 2\nBack to the Future 3\nBack to the Future 2")
        total = self.service.handle_cart()
        self.assertEqual(total, 48.00)

    def test_with_other_dvd(self):
        self.input_adapter.set_cart("Back to the Future 1\nBack to the Future 2\nBack to the Future 3\nLa chèvre")
        total = self.service.handle_cart()
        self.assertEqual(total, 56.00)

if __name__ == "__main__":
    unittest.main()
