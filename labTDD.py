import math

class MachinePowerCalculator:
        
        def GetPowerConsumption(self, machineType: str, duration: int, isEnergySaving: bool) -> float:
            if machineType == None or machineType == "":
                raise ValueError("Machine type cannot be empty.")
            
            if duration <= 0:
                raise ValueError("Duration must be greater than zero.")
            
            usedPower: float = 0.0
            if machineType == "MillingMachine":
                usedPower = 5.0 * duration
            elif machineType == "Lathe":
                usedPower = 3.5 * math.log(duration+1, 10)
            elif machineType == "Press":
                usedPower = 7.2 * duration
            else:
                raise ValueError("Invalid machine type.")
            
            return usedPower * (0.8 if isEnergySaving else 1.0)
                