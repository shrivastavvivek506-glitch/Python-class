class brand:
    brand_name = "Casio"

class modal:
    modal_name = "fx-991ES"

class color(brand, modal):
    color_name = "Black"

    def display(self):
        print("Brand Name:", self.brand_name)
        print("Modal Name:", self.modal_name)
        print("Color Name:", self.color_name)

c_obj = color()
print(c_obj.display())