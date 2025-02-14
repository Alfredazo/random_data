number = int(input("Digite un número: "))


# Calcular la cantidad de dígitos en el numero sin convertirlo a str
def count_digits(number):
    count = 0
    number = int(number)
    while number > 0:
        number = number // 10
        print("Número: ", number)
        count += 1
    return count


print("Cantidad de dígitos: ", count_digits(number))
