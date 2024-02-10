class Computer:
    """
    Represents a generic computer with brand and model attributes.
    :param brand: The brand of the computer.
    :param model: The model of the computer.
    """

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def __str__(self):
        """
        Return a string representation of the computer.
        :return: A string containing the brand and model of the computer.
        """
        return f"Brand: {self.brand}, Model: {self.model}"


class Desktop(Computer):
    """
    Represents a desktop computer, which is a type of Computer.
    :param brand: The brand of the desktop computer.
    :param model: The model of the desktop computer.
    :param cpu_volume: The volume of the CPU in liters.
    """

    def __init__(self, brand, model, cpu_volume):
        super().__init__(brand, model)
        self.cpu_volume = cpu_volume

    def __str__(self):
        """
        Return a string representation of the desktop computer.
        :return: A string containing the brand, model, and CPU volume of the desktop computer.
        """
        return super().__str__() + f", CPU Volume: {self.cpu_volume} L"


class Laptop(Computer):
    """
    Represents a laptop computer, which is a type of Computer.
    :param brand: The brand of the laptop computer.
    :param model: The model of the laptop computer.
    :param battery_duration: The duration of the battery in hours.
    """

    def __init__(self, brand, model, battery_duration):
        super().__init__(brand, model)
        self.battery_duration = battery_duration

    def __str__(self):
        """
        Return a string representation of the laptop computer.
        :return: A string containing the brand, model, and battery duration of the laptop computer.
        """
        return super().__str__() + f", Battery Duration: {self.battery_duration} h"
