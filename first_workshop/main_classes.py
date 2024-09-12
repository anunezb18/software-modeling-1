"""
This module contains an internal platform of arcade videogames machines

@Author: <anunezb@udistrital.edu.co>

Arcagames is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Arcagames is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with PyCalculator-UD. If not, see <https://www.gnu.org/licenses/>. 
"""

from typing import List


class Videogame:
    """This class represents a videogame"""

    def __init__(self, name: str, code: int, genre: str, year_release: int):
        self.name = name
        self.code = code
        self.genre = genre
        self.year_release = year_release

    def show_videogame(self):
        """This function shows the videogame"""
        print(
            f"(Name: {self.name}, ID: {self.code}, Genre: {self.genre}, Year of release: {self.year_release})"
        )


class ArcadeMachine:
    """This class represents an arcade machine"""

    def __init__(self, code: int, material: str, color: str):
        self.code = code
        self.material = material
        self.price = self.define_prices(material)
        self.color = color
        self.catalog = Catalog().videogames

    def show_machine(self):
        """This method shows the arcade machine"""
        print("Success purchase")
        print(self.material, self.price)

    def define_prices(self, material: str) -> int:
        """This method defines the price of the arcade machine.

        Args:
            material (str): The material of the arcade machine

        Returns:
            int: The price of the arcade machine
        """
        if material == "wood":
            return 150
        elif material == "aluminum":
            return 200
        elif material == "carbon_fiber":
            return 350
        else:
            raise ValueError("Invalid material")


class User:
    """This class represents a user of the system"""

    def __init__(self, name: str, address: str, phone: str, email: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Email: {self.email}"

    def add_videogame_to_catalog(
        self, arcade_machine: ArcadeMachine, videogame: Videogame
    ):
        """This function adds a videogame to the catalog

        Args:
            arcade_machine (ArcadeMachine): The arcade machine
            videogame (Videogame): The videogame to add
        """
        arcade_machine.catalog.append(videogame)


class Catalog:
    """This class represents a catalog of videogames"""

    def __init__(self):
        self.videogames = self.main_videogames()

    def show_catalog(self):
        """This function shows the catalog of videogames"""
        print("Catalog of videogames")
        for videogame in self.videogames:
            videogame.show_videogame()

    def search_videogame_by_name(self, name: str) -> Videogame:
        """This function searches a videogame by name

        Args:
            name (str): The name of the videogame

        Returns:
            Videogame: The videogame searched
        """
        for videogame in self.videogames:
            if videogame.name == name:
                return videogame
        raise ValueError("Videogame not found")

    def search_videogame_by_genre(self, genre: str) -> Videogame:
        """This function searches a videogame by genre

        Args:
            genre (str): The genre of the videogame

        Returns:
            Videogame: The videogame searched by the genre
        """
        for videogame in self.videogames:
            if videogame.genre == genre:
                return videogame
        raise ValueError("Videogame not found")

    @staticmethod
    def main_videogames() -> list:
        """This function instantiates the main videogames

        Returns:
            list: The list of videogames installed in the arcade machine
        """
        list_videogames = [
            Videogame("The Legend of Zelda", 2, "Action-adventure", 1986),
            Videogame("Metroid", 3, "Action-adventure", 1986),
            Videogame("Mega Man", 4, "Platform", 1987),
            Videogame("Final Fantasy", 5, "Role-playing", 1987),
            Videogame("Castlevania", 6, "Action-adventure", 1986),
            Videogame("Contra", 7, "Run and gun", 1987),
            Videogame("Street Fighter II", 8, "Fighting", 1991),
            Videogame("Double Dragon", 9, "Beat 'em up", 1987),
            Videogame("Dragon Quest", 10, "Role-playing", 1986),
            Videogame("Ninja Gaiden", 11, "Action", 1988),
            Videogame("Duck Hunt", 12, "Shooter", 1984),
            Videogame("Punch-Out!!", 13, "Sports", 1987),
            Videogame("Excitebike", 14, "Racing", 1984),
            Videogame("Kid Icarus", 15, "Action-adventure", 1986),
            Videogame("Bubble Bobble", 16, "Platform", 1986),
            Videogame("Tetris", 17, "Puzzle", 1984),
            Videogame("Gradius", 18, "Shoot 'em up", 1985),
            Videogame("Gauntlet", 19, "Dungeon crawl", 1985),
            Videogame("R.C. Pro-Am", 20, "Racing", 1988),
            Videogame("Blaster Master", 21, "Platform", 1988),
            Videogame("Bionic Commando", 22, "Platform", 1988),
            Videogame("Battletoads", 23, "Beat 'em up", 1991),
            Videogame("EarthBound", 24, "Role-playing", 1994),
            Videogame("Chrono Trigger", 25, "Role-playing", 1995),
            Videogame("The King of Fighters '94", 26, "Fighting", 1994),
            Videogame("Mortal Kombat", 27, "Fighting", 1992),
            Videogame("Pac-Man", 28, "Arcade", 1980),
            Videogame("Donkey Kong", 29, "Arcade", 1981),
            Videogame("Galaga", 30, "Arcade", 1981),
        ]
        return list_videogames


class Purchase:
    """This class represents a purchase of a videogame"""

    def __init__(self, user: User, arcade_machine: ArcadeMachine):
        self.user = user
        self.arcade_machine = arcade_machine

    def show_purchase(self):
        """This function shows the purchase"""
        print("Success purchase")
        print(
            f"User: {self.user}, Arcade machine: {self.arcade_machine.material}, {self.arcade_machine.color}"
        )


class Manager:
    """This class manages all purchases"""

    def __init__(self):
        self.purchases: List[Purchase] = []

    def add_purchase(self, purchase: Purchase):
        """This method adds a purchase to the list of purchases

        Args:
            purchase (Purchase): The purchase to add
        """
        self.purchases.append(purchase)

    def show_all_purchases(self):
        """This method shows all purchases"""
        if not self.purchases:
            print("No purchases have been made.")
        else:
            for purchase in self.purchases:
                purchase.show_purchase()
        with open("purchases.txt", "w", encoding="utf-8") as file:
            for purchase in self.purchases:
                file.write(
                    f"User: {purchase.user}, Arcade machine: {purchase.arcade_machine.material}, {purchase.arcade_machine.color}\n"
                )
