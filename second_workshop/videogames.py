"""
This module has a class to define the videogames of each type of arcade videogames machine.

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


class Videogames(ABC):
    """This class defines the videogames of each type of arcade videogames machine."""

    def __init__(
        self,
        name: str,
        storytelling_creator: str,
        graphics_creator: str,
        category: str,
        price: float,
        year: int,
    ):
        self.name = name
        self.storytelling_creator = storytelling_creator
        self.graphics_creator = graphics_creator
        self.category = category
        self.price = price
        self.year = year

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Storytelling creator: {self.storytelling_creator}, "
            f"Graphics creator: {self.graphics_creator}, Category: {self.category}, "
            f"Price: {self.price}, Year: {self.year}"
        )

class DancingVideogames(Videogames):
    """This class defines the dancing videogames."""
class ClassicalVideogames(Videogames):
    """This class defines the classical videogames."""
class RacingVideogames(Videogames):
    """This class defines the racing videogames."""
class ShootingVideogames(Videogames):
    """This class defines the shooting videogames."""
class VirtualReality(Videogames):
    """This class defines the virtual reality videogames."""
class VideogamesFactory:
    """This class defines the factory of videogames of each type of arcade videogames machine."""

    @staticmethod
    def create_videogames(
        machine_type: str,
        name: str,
        storytelling_creator: str,
        graphics_creator: str,
        category: str,
        price: float,
        year: int,
    ):
        """This method creates the videogames of each type of arcade videogames machine."""

        if machine_type == "dance":
            return DancingVideogames(
                name, storytelling_creator, graphics_creator, category, price, year
            )
        elif machine_type == "classical":
            return ClassicalVideogames(
                name, storytelling_creator, graphics_creator, category, price, year
            )
        elif machine_type == "racing":
            return RacingVideogames(
                name, storytelling_creator, graphics_creator, category, price, year
            )
        elif machine_type == "shooting":
            return ShootingVideogames(
                name, storytelling_creator, graphics_creator, category, price, year
            )
        elif machine_type == "virtualreality":
            return VirtualReality(
                name, storytelling_creator, graphics_creator, category, price, year
            )
