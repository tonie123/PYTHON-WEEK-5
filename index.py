class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self._battery = battery  # in %

    def make_call(self, number):
        return f"Calling {number} from {self.model}..."

    def charge(self):
        self._battery = 100
        return f"{self.model} is now fully charged."

    def battery_status(self):
        return f"{self.model} battery at {self._battery}%."
