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

    def return_vehicle(self):
        if self.is_rented == True:
            self.is_rented = False
            print("You have returned the vehicle")
        else:
            print("You didnt rent the vehicle")


class rental_agency:
    def __init__(self.vehicles):

    def (self):
