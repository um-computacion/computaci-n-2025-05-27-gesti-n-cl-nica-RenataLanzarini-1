from modelo.paciente import Paciente
from modelo.turno import Turno
from modelo.receta import Receta


class HistoriaClinica:
    def __init__(self,paciente:Paciente):
        if not isinstance(paciente, Paciente):
            raise ValueError("Debe proporcionar un objeto Paciente válido.")
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []
    
    def agregar_turno(self, turno: Turno):
        if not isinstance(turno, Turno):
            raise ValueError("Debe proporcionar un objeto Turno válido.")
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        if not isinstance(receta, Receta):
            raise ValueError("Debe proporcionar un objeto Receta válido.")
        self.__recetas.append(receta)

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()

    def obtener_recetas(self) -> list[Receta]:
        return self.__recetas.copy()

    def __str__(self) -> str:
        turnos_str = "\n  ".join(str(t) for t in self.__turnos)
        recetas_str = "\n  ".join(str(r) for r in self.__recetas)
        return (
            f"HistoriaClinica(\n"
            f"  Paciente({self.__paciente}),\n"
            f"  Turnos:\n  {turnos_str if turnos_str else 'Sin turnos'},\n"
            f"  Recetas:\n  {recetas_str if recetas_str else 'Sin recetas'}\n"
            f")"
        )