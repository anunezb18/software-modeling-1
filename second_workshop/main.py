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

from users import Catalog, Client
from videogames import VideogamesFactory
from machines import MachineFactory


def admin_mode(catalog: Catalog):
    """This function represents the admin mode of the system."""
    while True:
        print("\nAdmin Mode")
        print("1. Search by videogame count")
        print("2. Search by material")
        print("3. Search by videogame name")
        print("4. Exit to main menu")
        choice = input("Select an option (1-4): ")

        if choice == "4":
            break

        try:
            if choice == "1":
                count = int(input("Enter the number of videogames: "))
                results = catalog.search_by_videogame_count(count)
            elif choice == "2":
                material = input("Enter the material: ")
                results = catalog.search_by_material(material)
            elif choice == "3":
                videogame_name = input("Enter the name of the videogame: ")
                results = catalog.search_by_videogame_name(videogame_name)
            else:
                print("Invalid choice. Please select a valid option.")
                continue

            if results:
                print("\nSearch Results:")
                for machine in results:
                    print(machine)
            else:
                print("\nNo machines found matching the criteria.")
        except ValueError:
            print("Invalid input. Please enter the correct data type.")
        except Exception as e:  # pylint: disable=broad-except
            print(f"An error occurred: {e}")


def user_mode(catalog: Catalog):
    """This function represents the user mode of the system."""
    try:
        print("\nEnter your delivery details:")
        user_id = int(input("Enter your ID: "))
        user_name = input("Enter your name: ")
        user_email = input("Enter your email: ")
        user_phone = input("Enter your phone number: ")
        user_address = input("Enter your address: ")

        user = Client(user_id, user_name, user_email, user_phone, user_address)
        print(
            f"\nUser Details -> ID: {user.id_}, Name: {user.name}, Email: {user.email}, "
            f"Phone: {user.phone}, Address: {user.adress}"
        )
    except ValueError:
        print("Invalid input. Please enter the correct data type.")
        return
    except Exception as e:  # pylint: disable=broad-except
        print(f"An error occurred: {e}")
        return

    while True:
        print("\nUser Mode")
        print("1. Select machine type")
        print("2. Search by price range")
        print("3. Search by weight range")
        print("4. Search by power consumption range")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "5":
            print("Exiting...")
            break

        try:
            if choice == "1":
                while True:
                    print("\nArcade Machine Factory")
                    print("1. Dance Revolution")
                    print("2. Classical Arcade")
                    print("3. Shooting Machine")
                    print("4. Racing Machine")
                    print("5. Virtual Reality")
                    print("6. Exit")
                    machine_choice = input(
                        "Select the type of machine to create (1-6): "
                    )

                    if machine_choice == "6":
                        print("Exiting...")
                        break

                    name = input("Enter the name of the machine: ")

                    print("\nSelect the material of the machine:")
                    print("1. Wood")
                    print("2. Aluminium")
                    print("3. Carbon Fiber")
                    material_choice = input("Select the material (1-3): ")

                    if material_choice == "1":
                        material = "wood"
                    elif material_choice == "2":
                        material = "aluminium"
                    elif material_choice == "3":
                        material = "carbon fiber"
                    else:
                        print("Invalid choice. Please select a valid option.")
                        continue

                    color = input("Enter the color of the machine: ")

                    if machine_choice == "1":
                        machine = MachineFactory.create_machine(
                            "DanceRevolution", name, material, color
                        )
                    elif machine_choice == "2":
                        machine = MachineFactory.create_machine(
                            "ClassicalArcade", name, material, color
                        )
                    elif machine_choice == "3":
                        machine = MachineFactory.create_machine(
                            "ShootingMachine", name, material, color
                        )
                    elif machine_choice == "4":
                        machine = MachineFactory.create_machine(
                            "RacingMachine", name, material, color
                        )
                    elif machine_choice == "5":
                        machine = MachineFactory.create_machine(
                            "VirtualReality", name, material, color
                        )
                    else:
                        print("Invalid choice. Please select a valid option.")
                        continue

                    machine.define_values(
                        machine.base_price,
                        machine.weight,
                        machine.power_consumption,
                        machine.material,
                    )
                    print(machine)

                    while True:
                        print("\nManage Videogames")
                        print("1. Add a videogame")
                        print("2. Remove a videogame")
                        print("3. Finish")
                        manage_choice = input("Select an option (1-3): ")

                        if manage_choice == "1":
                            try:
                                videogame_name = input(
                                    "Enter the name of the videogame to add: "
                                )
                                videogame_storytelling_creator = input(
                                    "Enter the storytelling creator of the videogame: "
                                )
                                videogame_graphics_creator = input(
                                    "Enter the graphics creator of the videogame: "
                                )
                                videogame_category = input(
                                    "Enter the category of the videogame: "
                                )
                                videogame_price = float(
                                    input("Enter the price of the videogame: ")
                                )
                                videogame_year = int(
                                    input("Enter the year of the videogame: ")
                                )
                                print("\nSelect the resolution of the game:")
                                print("1. HD")
                                print("2. SH")
                                videogame_resolution_input = input(
                                    "Select the resolution of the game (1-2): "
                                )

                                if videogame_resolution_input == "1":
                                    videogame_resolution = "HD"
                                elif videogame_resolution_input == "2":
                                    videogame_resolution = "SH"
                                else:
                                    print(
                                        "Invalid choice. Please select a valid option."
                                    )
                                    continue

                                if type(machine).__name__ == "DanceRevolution":
                                    videogame_machine_type = "dance"
                                elif type(machine).__name__ == "ClassicalArcade":
                                    videogame_machine_type = "classical"
                                elif type(machine).__name__ == "RacingMachine":
                                    videogame_machine_type = "racing"
                                elif type(machine).__name__ == "ShootingMachine":
                                    videogame_machine_type = "shooting"
                                elif type(machine).__name__ == "VirtualReality":
                                    videogame_machine_type = "virtualreality"

                                videogame_added = VideogamesFactory.create_videogames(
                                    videogame_machine_type,
                                    videogame_name,
                                    videogame_storytelling_creator,
                                    videogame_graphics_creator,
                                    videogame_category,
                                    videogame_price,
                                    videogame_year,
                                )

                                print(videogame_added)

                                if videogame_added is not None:
                                    user.add_videogame_to_catalog(
                                        machine, videogame_added, videogame_resolution
                                    )
                                    print(f"Videogame '{videogame_name}' added.")
                                else:
                                    print("Error: Failed to create videogame.")
                            except ValueError:
                                print(
                                    "Invalid input. Please enter the correct data type."
                                )
                            except Exception as e:  # pylint: disable=broad-except
                                print(f"An error occurred: {e}")
                        elif manage_choice == "2":
                            try:
                                videogame_name = input(
                                    "Enter the name of the videogame to remove: "
                                )
                                print("\nSelect the resolution of the game to remove:")
                                print("1. HD")
                                print("2. SH")
                                videogame_resolution_input = input(
                                    "Select the resolution of the game (1-2): "
                                )

                                if videogame_resolution_input == "1":
                                    videogame_resolution = "HD"
                                elif videogame_resolution_input == "2":
                                    videogame_resolution = "SH"
                                else:
                                    print(
                                        "Invalid choice. Please select a valid option."
                                    )
                                    continue

                                for vg in machine.videogames:
                                    if vg.name == videogame_name:
                                        user.remove_videogame_from_catalog(
                                            machine, vg, videogame_resolution
                                        )
                                        print(f"Videogame '{videogame_name}' removed.")
                                        break
                                else:
                                    print(f"Videogame '{videogame_name}' not found.")
                            except ValueError:
                                print(
                                    "Invalid input. Please enter the correct data type."
                                )
                            except Exception as e:  # pylint: disable=broad-except
                                print(f"An error occurred: {e}")
                        elif manage_choice == "3":
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")

                    print("\nReturning to main menu...")
                    break

            elif choice == "2":
                min_price = float(input("Enter the minimum price: "))
                max_price = float(input("Enter the maximum price: "))
                results = catalog.search_by_price_range(min_price, max_price)
                if results:
                    print("\nSearch Results:")
                    for machine in results:
                        print(machine)
                else:
                    print("\nNo machines found matching the criteria.")

            elif choice == "3":
                min_weight = int(input("Enter the minimum weight: "))
                max_weight = int(input("Enter the maximum weight: "))
                results = catalog.search_by_weight_range(min_weight, max_weight)
                if results:
                    print("\nSearch Results:")
                    for machine in results:
                        print(machine)
                else:
                    print("\nNo machines found matching the criteria.")

            elif choice == "4":
                min_power = int(input("Enter the minimum power consumption: "))
                max_power = int(input("Enter the maximum power consumption: "))
                results = catalog.search_by_power_consumption_range(
                    min_power, max_power
                )
                if results:
                    print("\nSearch Results:")
                    for machine in results:
                        print(machine)
                else:
                    print("\nNo machines found matching the criteria.")

            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter the correct data type.")
        except Exception as e:  # pylint: disable=broad-except
            print(f"An error occurred: {e}")


def main():
    """This function represents the main menu of the system."""
    catalog = Catalog()

    # Initialize the catalog with some machines
    catalog.add_machine(
        MachineFactory.create_machine(
            "DanceRevolution", "DDR Machine", "aluminium", "red"
        )
    )
    catalog.add_machine(
        MachineFactory.create_machine(
            "ClassicalArcade", "Classic Machine", "wood", "blue"
        )
    )
    catalog.add_machine(
        MachineFactory.create_machine(
            "ShootingMachine", "Shooter Machine", "carbon fiber", "green"
        )
    )
    catalog.add_machine(
        MachineFactory.create_machine(
            "RacingMachine", "Racer Machine", "carbon fiber", "yellow"
        )
    )
    catalog.add_machine(
        MachineFactory.create_machine("VirtualReality", "VR Machine", "wood", "black")
    )

    while True:
        print("\nArcade Machine Catalog")
        print("1. Admin Mode")
        print("2. User Mode")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == "3":
            print("Exiting...")
            break

        try:
            if choice == "1":
                admin_mode(catalog)
            elif choice == "2":
                user_mode(catalog)
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter the correct data type.")
        except Exception as e:  # pylint: disable=broad-except
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
