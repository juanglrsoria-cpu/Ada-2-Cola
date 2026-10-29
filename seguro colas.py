class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        return self.elementos.copy()


# Crear colas para los servicios
servicios = {
    1: Cola(),
    2: Cola(),
    3: Cola()
}

# Contadores de turnos
contadores = {
    1: 0,
    2: 0,
    3: 0
}


def procesar_comando(comando):
    comando = comando.strip().upper()

    if len(comando) < 2:
        print("Comando invalido. Ejemplo: C1 o A1")
        return

    letra = comando[0]

    try:
        servicio = int(comando[1:])
    except ValueError:
        print("Debes ingresar un numero de servicio.")
        return

    if servicio not in servicios:
        print("Servicio inexistente. Usa 1, 2 o 3.")
        return

    if letra == "C":
        contadores[servicio] += 1
        turno = contadores[servicio]
        servicios[servicio].encolar(turno)

        print(
            f"Cliente registrado en servicio {servicio}. "
            f"Turno asignado: {turno}"
        )

    elif letra == "A":
        turno = servicios[servicio].desencolar()

        if turno is None:
            print(f"No hay clientes en el servicio {servicio}.")
        else:
            print(
                f"Llamando al turno {turno}, "
                f"servicio {servicio}."
            )

    else:
        print("Comando desconocido. Usa C para registrar o A para atender.")


print("=== SISTEMA DE ATENCION DE SEGUROS ===")
print("Servicios disponibles:")
print("1 - Autos")
print("2 - Vida")
print("3 - Hogar")
print()
print("C1, C2 o C3: registrar cliente")
print("A1, A2 o A3: atender cliente")
print("S: salir")
print()

while True:
    comando = input("Ingresa un comando: ").strip().upper()

    if comando == "S":
        print("Sistema finalizado.")
        break

    procesar_comando(comando)