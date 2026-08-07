class vehicle:
    company = "BMW"
class car:
    model = "BMW X5"

class bike(vehicle, car):
    color = "Black"

b_obj = bike()
print("Company Name:", b_obj.company)
print("Model Name:", b_obj.model)
print("Color Name:", b_obj.color)