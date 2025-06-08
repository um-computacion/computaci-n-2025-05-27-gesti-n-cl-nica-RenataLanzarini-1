from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not isinstance(paciente, Paciente):
            raise ValueError("Debe proporcionar un objeto Paciente válido.")
        if not isinstance(medico, Medico):
            raise ValueError("Debe proporcionar un objeto Medico válido.")
        if not isinstance(medicamentos, list) or not medicamentos:
            raise ValueError("La lista de medicamentos no puede estar vacía.")
        for med in medicamentos:
            if not isinstance(med, str) or not med.strip():
                raise ValueError("Cada medicamento debe ser una cadena no vacía.")

        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        meds = ", ".join(self.__medicamentos)
        return (
            f"Receta(\n"
            f"  Paciente({self.__paciente}),\n"
            f"  Medico({self.__medico}),\n"
            f"  Medicamentos: [{meds}],\n"
            f"  Fecha: {self.__fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f")"
        )
