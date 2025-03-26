class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def display_info(self):
        return f"Smartphone Info: {self.brand} {self.model}, Storage: {self.storage}GB"

class SmartDevice(Smartphone):
    def __init__(self, brand, model, storage, os):
        super().__init__(brand, model, storage)
        self.os = os

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, OS: {self.os}"