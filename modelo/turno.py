from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        if not isinstance(paciente, Paciente):
            raise ValueError("Debe proporcionar un objeto Paciente válido.")
        if not isinstance(medico, Medico):
            raise ValueError("Debe proporcionar un objeto Medico válido.")
        if not isinstance(fecha_hora, datetime):
            raise ValueError("La fecha y hora debe ser un objeto datetime.")
        if not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía.")

        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (
            f"Turno(\n"
            f"  Paciente({self.__paciente}),\n"
            f"  Medico({self.__medico}),\n"
            f"  {self.__fecha_hora},\n"
            f"  {self.__especialidad}\n"
            f")"
        )
