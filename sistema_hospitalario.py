class SensorBiomedico:
    def __init__(self, id_sensor, tipo, unidad_medida):
        self.__id_sensor = id_sensor
        self.__tipo = tipo
        self.__unidad_medida = unidad_medida

    # Getters
    def getIDSensor(self):
        return self.__id_sensor
    def getTipo(self):
        return self.__tipo
    def getUnidadMedida(self):
        return self.__unidad_medida

    # Setters
    def setIDSensor(self, id_sensor):
        self.__id_sensor = id_sensor
    def setTipo(self, tipo):
        self.__tipo = tipo
    def setUnidadMedida(self, unidad_medida):
        self.__unidad_medida = unidad_medida


class SensorCardiaco(SensorBiomedico):
    def __init__(self, id_sensor, tipo, unidad_medida, frecuencia_muestreo):
        super().__init__(id_sensor, tipo, unidad_medida)
        self.__frecuencia_muestreo = frecuencia_muestreo

    def getFrecuenciaMuestreo(self):
        return self.__frecuencia_muestreo
    def setFrecuenciaMuestreo(self, frecuencia):
        self.__frecuencia_muestreo = frecuencia


class SensorRespiratorio(SensorBiomedico):
    def __init__(self, id_sensor, tipo, unidad_medida, capacidad_flujo):
        super().__init__(id_sensor, tipo, unidad_medida)
        self.__capacidad_flujo = capacidad_flujo

    def getCapacidadFlujo(self):
        return self.__capacidad_flujo
    def setCapacidadFlujo(self, capacidad):
        self.__capacidad_flujo = capacidad


class SensorTemperatura(SensorBiomedico):
    def __init__(self, id_sensor, tipo, unidad_medida, rango_operacion):
        super().__init__(id_sensor, tipo, unidad_medida)
        self.__rango_operacion = rango_operacion  # tuple (min, max)

    def getRangoOperacion(self):
        return self.__rango_operacion
    def setRangoOperacion(self, rango):
        self.__rango_operacion = rango


# --- Crear objetos y mostrar datos ---
cardiaco = SensorCardiaco("C001", "Cardíaco", "Hz", 250)
respiratorio = SensorRespiratorio("R001", "Respiratorio", "L/min", 40)
temperatura = SensorTemperatura("T001", "Temperatura", "°C", (35, 42))

print("Cardiaco:", cardiaco.getIDSensor(), cardiaco.getTipo(),
      cardiaco.getUnidadMedida(), cardiaco.getFrecuenciaMuestreo())
print("Respiratorio:", respiratorio.getIDSensor(), respiratorio.getTipo(),
      respiratorio.getUnidadMedida(), respiratorio.getCapacidadFlujo())
print("Temperatura:", temperatura.getIDSensor(), temperatura.getTipo(),
      temperatura.getUnidadMedida(), temperatura.getRangoOperacion())

# Demostración de que el atributo privado no es accesible
try:
    print(cardiaco.__id_sensor)
except AttributeError as e:
    print("Acceso directo falló:", e)
