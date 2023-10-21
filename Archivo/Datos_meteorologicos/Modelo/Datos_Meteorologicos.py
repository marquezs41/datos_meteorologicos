class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]:
        estadisticas_calculadas:list = []
        with open("datos.txt", "r") as archivo:
            for Datos in archivo:
                print(Datos)