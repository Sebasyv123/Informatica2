#Julián Pino
#Sebastián Yepes

# ==============================
#   Clases de Sensores
# ==============================

class SensorBiomedico:
    def __init__(self, id_sensor, tipo, unidad_medida):
        # Atributos privados (encapsulación con __)
        self.__id_sensor = id_sensor
        self.__tipo = tipo
        self.__unidad_medida = unidad_medida

    # Getters para acceder a atributos privados
    def getIDSensor(self):
        return self.__id_sensor
    def getTipo(self):
        return self.__tipo
    def getUnidadMedida(self):
        return self.__unidad_medida

    # Setters para modificar atributos privados
    def setIDSensor(self, id_sensor):
        self.__id_sensor = id_sensor
    def setTipo(self, tipo):
        self.__tipo = tipo
    def setUnidadMedida(self, unidad_medida):
        self.__unidad_medida = unidad_medida

    def __str__(self):
        return (f"ID: {self.getIDSensor()} | Tipo: {self.getTipo()} "
                f"| Unidad: {self.getUnidadMedida()}")


class SensorCardiaco(SensorBiomedico):
    def __init__(self, id_sensor, unidad_medida, frecuencia_muestreo):
        super().__init__(id_sensor, "Cardiaco", unidad_medida)
        self.__frecuencia_muestreo = frecuencia_muestreo

    def getFrecuenciaMuestreo(self):
        return self.__frecuencia_muestreo
    def setFrecuenciaMuestreo(self, frecuencia):
        self.__frecuencia_muestreo = frecuencia

    def __str__(self):
        base = super().__str__()
        return f"{base} | Frecuencia muestreo: {self.getFrecuenciaMuestreo()} Hz"


class SensorRespiratorio(SensorBiomedico):
    def __init__(self, id_sensor, unidad_medida, capacidad_flujo):
        super().__init__(id_sensor, "Respiratorio", unidad_medida)
        self.__capacidad_flujo = capacidad_flujo

    def getCapacidadFlujo(self):
        return self.__capacidad_flujo
    def setCapacidadFlujo(self, capacidad):
        self.__capacidad_flujo = capacidad

    def __str__(self):
        base = super().__str__()
        return f"{base} | Capacidad flujo: {self.getCapacidadFlujo()} L/min"


class SensorTemperatura(SensorBiomedico):
    def __init__(self, id_sensor, unidad_medida, rango_operacion):
        super().__init__(id_sensor, "Temperatura", unidad_medida)
        self.__rango_operacion = rango_operacion  # tuple (min, max)

    def getRangoOperacion(self):
        return self.__rango_operacion
    def setRangoOperacion(self, rango):
        self.__rango_operacion = rango

    def __str__(self):
        base = super().__str__()
        rmin, rmax = self.getRangoOperacion()
        return f"{base} | Rango operación: {rmin}°C – {rmax}°C"


# ==============================
#   Sistema de Monitoreo
# ==============================

class SistemaMonitoreo:
    def __init__(self):
        # Lista que almacenará los sensores creado
        self.sensores = []

    def agregar_sensor(self, sensor):
        # Evitar ID duplicado
        if any(s.getIDSensor() == sensor.getIDSensor() for s in self.sensores):
            print("Sensor con ID ya registrado.")
            return
        self.sensores.append(sensor)
        print("Sensor agregado.")

    def ver_datos_sensor(self, id_sensor):
        for s in self.sensores:
            if s.getIDSensor() == id_sensor:
                return str(s)
        return "Sensor no encontrado."

    def contar_sensores(self):
        return len(self.sensores)


# ==============================
#   Función principal con menú
# ==============================

def main():
    sistema = SistemaMonitoreo()

    while True:
        print("\n--- Menú de Sistema de Monitoreo ---")
        print("1. Agregar sensor")
        print("2. Ver datos de un sensor")
        print("3. Contar sensores")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            tipo = input("Tipo de sensor (Cardiaco/Respiratorio/Temperatura): ").strip().lower()
            id_sensor = input("ID del sensor: ").strip()
            unidad_medida = input("Unidad de medida: ").strip()

            if tipo == 'cardiaco':
                try:
                    frecuencia = float(input("Frecuencia de muestreo (Hz): "))
                    sensor = SensorCardiaco(id_sensor, unidad_medida, frecuencia)
                    sistema.agregar_sensor(sensor)
                except ValueError:
                    print("Frecuencia inválida.")
            elif tipo == 'respiratorio':
                try:
                    capacidad = float(input("Capacidad de flujo (L/min): "))
                    sensor = SensorRespiratorio(id_sensor, unidad_medida, capacidad)
                    sistema.agregar_sensor(sensor)
                except ValueError:
                    print("Capacidad inválida.")
            elif tipo == 'temperatura':
                try:
                    min_rango = float(input("Rango mínimo de operación (°C): "))
                    max_rango = float(input("Rango máximo de operación (°C): "))
                    sensor = SensorTemperatura(id_sensor, unidad_medida, (min_rango, max_rango))
                    sistema.agregar_sensor(sensor)
                except ValueError:
                    print("Valores de rango inválidos.")
            else:
                print("Tipo de sensor no válido.")

        elif opcion == '2':
            id_sensor = input("Ingrese el ID del sensor: ").strip()
            print(sistema.ver_datos_sensor(id_sensor))

        elif opcion == '3':
            print(f"Número total de sensores registrados: {sistema.contar_sensores()}")

        elif opcion == '4':
            print("Saliendo del sistema…")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


# Solo ejecutar el menú si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
