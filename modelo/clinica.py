from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.especialidad import Especialidad
from modelo.historia_clinica import HistoriaClinica
from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class Clinica:
    def __init__(self):
        self.__pacientes = {}  # DNI -> Paciente
        self.__medicos = {}    # Matrícula -> Medico
        self.__turnos = []     # Lista de Turno
        self.__historias_clinicas = {}  # DNI -> HistoriaClinica

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError(f"Ya existe un paciente con DNI {dni}.")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError(f"Ya existe un médico con matrícula {matricula}.")
        self.__medicos[matricula] = medico

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        medico = self.__medicos[matricula]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)

        paciente = self.__pacientes[dni]
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        if not medicamentos:
            raise RecetaInvalidaException("La receta no puede estar vacía.")

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        self.validar_existencia_medico(matricula)
        return self.__medicos[matricula]

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()

    def obtener_historia_clinica_por_dni(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]

    # Utilidades y validaciones
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"No se encontró paciente con DNI {dni}.")

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException(f"No se encontró médico con matrícula {matricula}.")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos:
            if (
                turno.obtener_medico().obtener_matricula() == matricula
                and turno.obtener_fecha_hora() == fecha_hora
            ):
                raise TurnoOcupadoException("El médico ya tiene un turno agendado en esa fecha y hora.")

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]
        def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str | None:
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        especialidad_del_dia = self.obtener_especialidad_disponible(medico, dia_semana)
        if especialidad_del_dia is None:
            raise MedicoNoDisponibleException(f"El médico no atiende ningún día los {dia_semana}.")
        if especialidad_del_dia.lower() != especialidad_solicitada.lower():
            raise MedicoNoDisponibleException(
                f"El médico no atiende la especialidad '{especialidad_solicitada}' el día {dia_semana}."
            )
