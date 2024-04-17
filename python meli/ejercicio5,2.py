import random

def tirar_moneda():
    """Función para simular la tirada de una moneda."""
    # Generar un número aleatorio (0 o 1) para representar cara o cruz
    resultado = random.randint(0, 1)
    if resultado == 0:
        return 'cara'
    else:
        return 'cruz'

# Tirar la moneda
resultado_moneda = tirar_moneda()

# Solicitar al jugador que apueste por cara o cruz
apuesta = input("Apuesta por cara o cruz: ").lower()

# Verificar si la apuesta del jugador es correcta
if apuesta == resultado_moneda:
    print("¡Felicitaciones! Has acertado. La moneda cayó en", resultado_moneda)
else:
    print("Perdiste. La moneda cayó en", resultado_moneda)