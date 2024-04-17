import random

def tirar_dado():
    """Función para simular la tirada de un dado."""
    # Generar un número aleatorio entre 1 y 6 para representar el valor del dado
    return random.randint(1, 6)

# Tirar el dado
resultado_dado = tirar_dado()

# Solicitar al jugador que apueste por un valor entre 1 y 6
apuesta = int(input("Apuesta por un valor entre 1 y 6: "))

# Verificar si la apuesta del jugador es correcta
if apuesta == resultado_dado:
    print("¡Felicidades! Has acertado. El dado mostró un", resultado_dado)
else:
    print("Perdiste. El dado mostró un", resultado_dado)