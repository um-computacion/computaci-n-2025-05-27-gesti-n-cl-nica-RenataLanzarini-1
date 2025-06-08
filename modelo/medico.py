from modelo.especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list[Especialidad] = None):
        if not nombre.strip():
            raise ValueError("El nombre del médico no puede estar vacío.")
        if not matricula.strip().isdigit():
            raise ValueError("La matrícula debe ser numérica.")

        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades if especialidades else []

    def agregar_especialidad(self, especialidad: Especialidad):
        tipos_actuales = [e.obtener_especialidad().lower() for e in self.__especialidades]
        if especialidad.obtener_especialidad().lower() in tipos_actuales:
            raise ValueError("El médico ya tiene esta especialidad.")
        self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None

    def __str__(self) -> str:
        especialidades_str = "\n  ".join(str(e) for e in self.__especialidades)
        return f"{self.__nombre}, {self.__matricula}, [\n  {especialidades_str}\n]"
