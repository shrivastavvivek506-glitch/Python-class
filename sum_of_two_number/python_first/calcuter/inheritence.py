class grandfather:
    son_in_low = "vivek Shrivastav"
    vehicle = "car"

class father(grandfather):
    daughter = "sonakshi Shrivastav"
    gift = "bike"

class son(father):
    trivel = "Sonakshi Shrivastav ❤️, vivek Shrivastav"
    second_gift = " BMW car"

s_obj = son()
print(s_obj.trivel)
print(s_obj.daughter)
print(s_obj.son_in_low)
print(s_obj.vehicle)
print(s_obj.second_gift)