class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre.strip():
            raise ValueError("El nombre del paciente no puede estar vacío.")
        if not dni.strip().isdigit():
            raise ValueError("El DNI debe ser numérico.")
        if not self._validar_fecha(fecha_nacimiento):
            raise ValueError("La fecha debe tener el formato dd/mm/aaaa.")

        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni

    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"

    def _validar_fecha(self, fecha: str) -> bool:
        import re
        return bool(re.match(r"\d{2}/\d{2}/\d{4}", fecha))
