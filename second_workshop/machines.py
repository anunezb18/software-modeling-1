"""
This module has a class to define a general arcade videogames machine.

Author: Alejandro Nuñez <anunezb@udistrital.edu.co>

This file is part of Workshop-2.

Workshop-2 is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Workshop-2 is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Workshop-SM-UD. If not, see <https://www.gnu.org/licenses/>. 
"""

from abc import ABC

class Machine(ABC):
    """This class defines a general arcade videogames machine."""

    def __init__(
        self,
        name: str,
        material: str,
        dimensions: str,
        weight: int,
        power_consumption: int,
        memory: str,
        processor: str,
        base_price: float,
        videogames: str,
    ):
        self.name = name
        self.material = material
        self.dimensions = dimensions
        self.weight = weight
        self.power_consumption = power_consumption
        self.memory = memory
        self.processor = processor
        self.base_price = base_price
        self.videogames = videogames

    def define_values(
        self, base_price: float, weight: int, power_consumption: int, material: str
    ):
        """This method defines the values of the machine according to the material used."""

        if material == "wood":
            self.weight = weight * (1 + 0.1)
            self.base_price = base_price * (1 - 0.05)
            self.power_consumption = power_consumption * (1 + 0.15)
        elif material == "aluminium":
            self.weight = weight * (1 - 0.05)
            self.base_price = base_price * (1 + 0.1)
        elif material == "carbon_fiber":
            self.weight = weight * (1 - 0.15)
            self.base_price = base_price * (1 + 0.2)
            self.power_consumption = power_consumption * (1 - 0.1)


class DanceRevolution(Machine):
    """This class defines a Dance Revolution arcade videogames machine."""

    def __init__(self, name: str, material: str, videogames: str):
        super().__init__(
            name=name,
            material=material,
            dimensions="3*2*5",
            weight=300,
            power_consumption=500,
            memory="32gb",
            processor="Intel Celeron",
            base_price=280.0,
            videogames=videogames,
        )
        self.difficulties = ["easy", "medium", "hard"]
        self.arrow_cardinalities = ["up", "down", "left", "right"]
        self.controls_price = 50


class ClassicalArcade(Machine):
    """This class defines a Classical Arcade arcade videogames machine."""

    def __init__(self, name: str, material: str, videogames: str):
        super().__init__(
            name=name,
            material=material,
            dimensions="2*2*5",
            weight=350,
            power_consumption=100,
            memory="8gb",
            processor="x86",
            base_price=300.0,
            videogames=videogames,
        )
        self.make_vibration = False
        self.sound_record_alert = False

    def enable_vibration(self):
        """This method enables the vibration of the machine."""
        self.make_vibration = True

    def disable_vibration(self):
        """This method disables the vibration of the machine."""
        self.make_vibration = False

    def enable_sound_record_alert(self):
        """This method enables the sound record alert of the machine."""
        self.sound_record_alert = True

    def disable_sound_record_alert(self):
        """This method disables the sound record alert of the machine."""
        self.sound_record_alert = False


class ShootingMachine(Machine):
    """This class defines a Shooting Machine arcade videogames machine."""

    def __init__(self, name: str, material: str, videogames: str):
        super().__init__(
            name=name,
            material=material,
            dimensions="2*2*2",
            weight=200,
            power_consumption=300,
            memory="16gb",
            processor="Intel Pentium",
            base_price=250.0,
            videogames=videogames,
        )
        self.gun_type = "pistol"
        self.gun_price = 40


class RacingMachine(Machine):
    """This class defines a Racing Machine arcade videogames machine."""

    def __init__(self, name: str, material: str, videogames: str):
        super().__init__(
            name=name,
            material=material,
            dimensions="2*2*4",
            weight=400,
            power_consumption=350,
            memory="4gb",
            processor="Zilog Z80",
            base_price=350.0,
            videogames=videogames,
        )
        self.type_vehicle = "car"
        self.seats = 1


class VirtualReality(Machine):
    """This class defines a Virtual Reality arcade videogames machine."""

    def __init__(self, name: str, material: str, videogames: str):
        super().__init__(
            name=name,
            material=material,
            dimensions="0.15*0.09*0.10",
            weight=30,
            power_consumption=50,
            memory="64gb",
            processor="Meta Quest",
            base_price=600.0,
            videogames=videogames,
        )
        self.type_glasses = "VR"
        self.resolution_glasses = "1080p"
        self.price_glasses = 100


class MachineFactory:
    """This class is a factory to create machines of different types."""

    @staticmethod
    def create_machine(machine_type: str, name: str, material: str, videogames: str):
        """This method creates a machine of the specified type."""
        if machine_type == "DanceRevolution":
            return DanceRevolution(name, material, videogames)
        elif machine_type == "ClassicalArcade":
            return ClassicalArcade(name, material, videogames)
        elif machine_type == "ShootingMachine":
            return ShootingMachine(name, material, videogames)
        elif machine_type == "RacingMachine":
            return RacingMachine(name, material, videogames)
        elif machine_type == "VirtualReality":
            return VirtualReality(name, material, videogames)
