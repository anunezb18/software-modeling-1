"""
This module has a class to define a general arcade videogames machine.

Author: Alejandro Nuñez <anunezb@udistrital.edu.co>

This file is part of Arcagames-2.

Arcagames-2 is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Arcagames-2 is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Arcagames-2. If not, see <https://www.gnu.org/licenses/>. 
"""

from abc import ABC
from typing import List
from videogames import VideogamesFactory, Videogames


class Machine(ABC):
    """This class defines a general arcade videogames machine."""

    def __init__(
        self,
        name: str,
        material: str,
        color: str,
        dimensions: str,
        weight: int,
        power_consumption: int,
        memory: str,
        processor: str,
        base_price: float,
        videogames: List[Videogames],
    ):
        self.name = name
        self.material = material
        self.color = color
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

    def show_by_amount_of_videogames(self, amount: int):
        """This method shows the videogames of the machine according to the amount specified."""
        return [game for game in self.videogames if game.price > amount]

    def __str__(self) -> str:
        videogames_str = "\n".join(str(game) for game in self.videogames)
        return (
            f"\nMachine Details:\n"
            f"Type: {type(self).__name__}\n"
            f"Name: {self.name}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Dimensions: {self.dimensions}\n"
            f"Weight: {self.weight} kg\n"
            f"Power Consumption: {self.power_consumption} W\n"
            f"Memory: {self.memory}\n"
            f"Processor: {self.processor}\n"
            f"Base Price: ${self.base_price}\n"
            f"Videogames:\n{videogames_str}"
        )


class DanceRevolution(Machine):
    """This class defines a Dance Revolution arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="3*2*5",
            weight=300,
            power_consumption=500,
            memory="32gb",
            processor="Intel Celeron",
            base_price=280.0,
            videogames=[
                VideogamesFactory.create_videogames(
                    "dance",
                    "Move your body",
                    "Konami",
                    "Rythm Tech",
                    "Rythm/Dance",
                    50.0,
                    2019,
                ),
                VideogamesFactory.create_videogames(
                    "dance",
                    "Dancing in the moon",
                    "Groove Studios",
                    "Pulse Visuals",
                    "Dance/Music",
                    60.0,
                    2022,
                ),
            ],
        )
        self.difficulties = ["easy", "medium", "hard"]
        self.arrow_cardinalities = ["up", "down", "left", "right"]
        self.controls_price = 50

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nDifficulties: {self.difficulties}\n"
            f"Arrow Cardinalities: {self.arrow_cardinalities}\n"
            f"Controls Price: ${self.controls_price}"
        )


class ClassicalArcade(Machine):
    """This class defines a Classical Arcade arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="2*2*5",
            weight=350,
            power_consumption=100,
            memory="8gb",
            processor="x86",
            base_price=300.0,
            videogames=[
                VideogamesFactory.create_videogames(
                    "classical",
                    "Super Mario Bros",
                    "Atari",
                    "Pixel Masters",
                    "Action/Adventure",
                    35.0,
                    1990,
                ),
                VideogamesFactory.create_videogames(
                    "classical",
                    "Prince of Persa",
                    "Namco",
                    "Retro Visuals",
                    "Puzzle/Strategy",
                    40.0,
                    1988,
                ),
            ],
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

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nMake Vibration: {self.make_vibration}\n"
            f"Sound Record Alert: {self.sound_record_alert}"
        )


class ShootingMachine(Machine):
    """This class defines a Shooting Machine arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="2*2*2",
            weight=200,
            power_consumption=300,
            memory="16gb",
            processor="Intel Pentium",
            base_price=250.0,
            videogames=[
                VideogamesFactory.create_videogames(
                    "shooting",
                    "Doom",
                    "Capcom",
                    "Blaster Studios",
                    "Shooter/Action",
                    55.0,
                    2007,
                ),
                VideogamesFactory.create_videogames(
                    "shooting",
                    "Resident Evil",
                    "SNK",
                    "Bullet Visuals",
                    "Arcade/Shooter",
                    65.0,
                    2015,
                ),
            ],
        )
        self.gun_type = "pistol"
        self.gun_price = 40

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nGun Type: {self.gun_type}\n"
            f"Gun Price: ${self.gun_price}"
        )


class RacingMachine(Machine):
    """This class defines a Racing Machine arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="2*2*4",
            weight=400,
            power_consumption=350,
            memory="4gb",
            processor="Zilog Z80",
            base_price=350.0,
            videogames=[
                VideogamesFactory.create_videogames(
                    "racing",
                    "Sonic Speed Game",
                    "Sega",
                    "Speed Visuals",
                    "Racing/Simulation",
                    45.0,
                    2006,
                ),
                VideogamesFactory.create_videogames(
                    "racing",
                    "Need for Speed",
                    "Electronic Arts",
                    "Turbo Graphics",
                    "Racing/Arcade",
                    60.0,
                    2010,
                ),
            ],
        )
        self.type_vehicle = "car"
        self.seats = 1

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nType Vehicle: {self.type_vehicle}\n"
            f"Seats: {self.seats}"
        )


class VirtualReality(Machine):
    """This class defines a Virtual Reality arcade videogames machine."""

    def __init__(self, name: str, material: str, color: str):
        super().__init__(
            name=name,
            material=material,
            color=color,
            dimensions="0.15*0.09*0.10",
            weight=30,
            power_consumption=50,
            memory="64gb",
            processor="Meta Quest",
            base_price=600.0,
            videogames=[
                VideogamesFactory.create_videogames(
                    "virtualreality",
                    "Meta Game",
                    "Meta",
                    "Meta Visuals",
                    "VR/Simulation",
                    105.0,
                    2023,
                ),
                VideogamesFactory.create_videogames(
                    "virtualreality",
                    "Batman VR",
                    "Electronic Arts",
                    "EA Montreal",
                    "VR/Simulation",
                    150.0,
                    2024,
                ),
            ],
        )
        self.type_glasses = "VR"
        self.resolution_glasses = "1080p"
        self.price_glasses = 100

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nType Glasses: {self.type_glasses}\n"
            f"Resolution Glasses: {self.resolution_glasses}\n"
            f"Price Glasses: ${self.price_glasses}"
        )


class MachineFactory:
    """This class is a factory to create machines of different types."""

    @staticmethod
    def create_machine(machine_type: str, name: str, material: str, color: str):
        """This method creates a machine of the specified type."""
        if machine_type == "DanceRevolution":
            return DanceRevolution(name, material, color)
        elif machine_type == "ClassicalArcade":
            return ClassicalArcade(name, material, color)
        elif machine_type == "ShootingMachine":
            return ShootingMachine(name, material, color)
        elif machine_type == "RacingMachine":
            return RacingMachine(name, material, color)
        elif machine_type == "VirtualReality":
            return VirtualReality(name, material, color)
