import unittest
from labTDD import MachinePowerCalculator

class TestMachinePowerCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = MachinePowerCalculator()

    def test_empty_machine_type(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.GetPowerConsumption("", 10, False)
        self.assertEqual(str(context.exception), "Machine type cannot be empty.")

    def test_none_machine_type(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.GetPowerConsumption(None, 10, False)
        self.assertEqual(str(context.exception), "Machine type cannot be empty.")

    def test_negative_duration(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.GetPowerConsumption("MillingMachine", -5, False)
        self.assertEqual(str(context.exception), "Duration must be greater than zero.")

    def test_invalid_machine_type(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.GetPowerConsumption("InvalidMachine", 10, False)
        self.assertEqual(str(context.exception), "Invalid machine type.")

    def test_milling_machine_power(self):
        power = self.calculator.GetPowerConsumption("MillingMachine", 10, False)
        self.assertEqual(power, 50.0)  # 5.0 * 10 * 1.0

    def test_lathe_power(self):
        power = self.calculator.GetPowerConsumption("Lathe", 10, False)
        self.assertEqual(power, 3.64)  # 3.5 * log(10+1) * 1.0

    def test_press_power(self):
        power = self.calculator.GetPowerConsumption("Press", 10, False)
        self.assertEqual(power, 72.0)  # 7.2 * 10 * 1.0

    def test_energy_saving_mode(self):
        power = self.calculator.GetPowerConsumption("MillingMachine", 10, True)
        self.assertEqual(power, 40.0)  # 5.0 * 10 * 0.8

if __name__ == "__main__":
    unittest.main()
