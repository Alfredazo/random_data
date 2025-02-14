# Validaciones
# Prender una ampolleta
# LUZ - Foco - Bombillo - circuito

esta_encendido = True
hay_luz = False
foco_quemado = False
circuito_quemado = False

# JS:
# let esta_encendido = false;

# Python:
# esta_encendido = False

# .Net
# bool esta_encendido = false;

# || = OR  -  && = AND


def prender():
    if esta_encendido == True and hay_luz == True:
        return "La ampolleta está encendida"
    else:
        if foco_quemado == True:
            return "El foco está quemado"
        else:
            return "No hay foco"


def parar_hasta_que_se_arregle():
    circuito_quemado = input("¿El circuito está quemado? (True/False): ") == "True"
    if circuito_quemado == True:
        return "No se puede prender la ampolleta"
    else:
        return prender()


print("Ampolleta encendida: ", parar_hasta_que_se_arregle())
