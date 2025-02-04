from models.FormSubmit import FormSubmit
from models.RandomData import RandomData

randomData = RandomData("es_MX")
formSubmit = FormSubmit(
    "https://docs.google.com/forms/d/e/1FAIpQLSfgNDfredza8QsHs5ZxioHLGT61jzRDSM2TagqtWaLZWjisZQ/formResponse"
)

print("Random name: ", randomData.generate_base_on_quantity(3))
# print("Form submit: ", formSubmit.submit("Juan", "Pepsi"))
print(
    "Form submit multiple: ",
    formSubmit.process_multiple_request_with_time(randomData.generate_base_on_quantity(20), 3),
)
