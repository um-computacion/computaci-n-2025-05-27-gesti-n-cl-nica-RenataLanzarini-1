class Paciente: 
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre.strip():
            raise valueError("El nombre del paciente del paciente no puede estar vacio.")
        if not dni.strip().isdigit():
            raise("El DNI debe ser númerico.")
        if not self._validar_fecha(fecha_nacimiento):
            raise valueError("La fecha debe tener el formato dd/mm/aaaa.")

        self.__nombre: nombre
        self.__dni: dni
        self.__fecha_nacimiento: fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni
    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"
    def _validar _fecha(self, fecha: str) -> bool:
        import re
        return bool(re.match(r"\d{2}/\{2}/\{4}", fecha))
        