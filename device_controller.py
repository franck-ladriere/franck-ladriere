# device_controller.py

class SmartDevice:
    def __init__(self, name, status="off"):
        self.name = name
        self.status = status

    def turn_on(self):
        self.status = "on"
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.status = "off"
        print(f"{self.name} is now OFF.")

# Exemple d'utilisation
if __name__ == "__main__":
    light = SmartDevice("Living Room Light")
    light.turn_on()
