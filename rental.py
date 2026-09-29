import json


class vehicle:
    def __init__(self, vehicle_id, make_model, daily_rate):
        self.vehicle_id = vehicle_id
        self.make_model = make_model
        self.daily_rate = daily_rate
        self.is_rented = False

    def get_details(self):
        status = " rented" if self.is_rented else "available"
        print(
            f"The {self.vehicle_id} of model {self.make_model} with daily rate {self.daily_rate} is currently {status}")

    def rent_vehicle(self, days):
        if self.is_rented == False:
            self.is_rented = True
            Total_bill = self.daily_rate*days
            print(Total_bill)
        else:
            print("Vehicle is already rented")

    def return_vehicle(self):
        if self.is_rented == True:
            self.is_rented = False
            print("You have returned the vehicle")
        else:
            print("You didnt rent the vehicle")

    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "make_model": self.make_model,
            "daily_rate": self.daily_rate,
            "status": self.is_rented
        }


class rental_agency:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle_to_add):
        self.vehicles.append(vehicle_to_add)
        print("Vehicle added successfully")

    def display_vehicles(self):
        available_vehicles = [
            item for item in self.vehicles if not item.is_rented]

        if not available_vehicles:
            print("No vehicles are currently available for rent.")
        else:
            print("\n--- Available Vehicles ---")
            for item in available_vehicles:
                item.get_details()

    def find_vehicles(self, vehicle_id):
        for item in self.vehicles:
            if item.vehicle_id.lower() == vehicle_id.lower():
                return item
        return None

    def save_to_json(self, filename="vehicles.json"):
        data = [item.to_dict() for item in self.vehicles]
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Fleet saved successfully.")

    def load_from_json(self, filename="vehicles.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.vehicles = []
                for item in data:
                    new_vehicle = vehicle(
                        item["vehicle_id"],
                        item["make_model"],
                        float(item["daily_rate"])
                    )
                    new_vehicle.is_rented = item["status"]
                    self.vehicles.append(new_vehicle)
            print("Fleet loaded successfully.")
        except FileNotFoundError:
            self.vehicles = []
            print("No save file found. Starting with an empty fleet.")


# --- Main CLI Execution ---
agency = rental_agency()
agency.load_from_json()

while True:
    print("\n=== Vehicle Rental System ===")
    print("1. Add Vehicle")
    print("2. Display Available Vehicles")
    print("3. Rent Vehicle")
    print("4. Return Vehicle")
    print("5. Exit & Save")

    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
        v_id = input("Enter Vehicle ID: ").strip()
        model = input("Enter Make & Model: ").strip()
        try:
            rate = float(input("Enter Daily Rate ($): ").strip())
            new_v = vehicle(v_id, model, rate)
            agency.add_vehicle(new_v)
        except ValueError:
            print("Invalid input for daily rate. Please enter a valid number.")

    elif choice == "2":
        agency.display_vehicles()

    elif choice == "3":
        v_id = input("Enter Vehicle ID to rent: ").strip()
        found = agency.find_vehicles(v_id)
        if found:
            try:
                days = int(input("Enter number of rental days: ").strip())
                found.rent_vehicle(days)
            except ValueError:
                print("Invalid number of days.")
        else:
            print("Vehicle not found.")

    elif choice == "4":
        v_id = input("Enter Vehicle ID to return: ").strip()
        found = agency.find_vehicles(v_id)
        if found:
            found.return_vehicle()
        else:
            print("Vehicle not found.")

    elif choice == "5":
        agency.save_to_json()
        print("Goodbye!")
        break

    else:
        print("Invalid selection. Please choose an option from 1 to 5.")
