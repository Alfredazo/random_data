from models.RandomData import RandomData

randomData = RandomData("es_MX")

print("Random name: ", randomData.generate_base_on_quantity(50))
