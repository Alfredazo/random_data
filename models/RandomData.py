from faker import Faker


class RandomData:

    drinks_dict = {
        0: "Coca Cola",
        1: "Pepsi",
        2: "Fanta",
        3: "Horchata",
        4: "Limonada",
        5: "Agua",
        6: "Ninguna",
    }

    def __init__(self, region="en_US"):
        self.fake = Faker([region])

    def generate_random_name(self):
        return self.fake.name()

    def generate_random_data_with_drink(self):
        bebida = self.drinks_dict[self.fake.random_int(0, 6)]
        return {"nombre:": self.fake.name(), "bebida": bebida}

    def generate_base_on_quantity(self, quantity):
        lst = []
        for _ in range(quantity):
            temp_data = self.generate_random_data_with_drink()
            print(temp_data)
            lst.append(temp_data)
        return lst
