from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import *

from datetime import datetime

class InterfazUsuario:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad a médico")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.agregar_especialidad()
            elif opcion == "5":
                self.emitir_receta()
            elif opcion == "6":
                self.ver_historia_clinica()
            elif opcion == "7":
                self.ver_turnos()
            elif opcion == "8":
                self.ver_pacientes()
            elif opcion == "9":
                self.ver_medicos()
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    # Implementaciones básicas (ej: agregar paciente)
    def agregar_paciente(self):
        try:
            nombre = input("Nombre del paciente: ")
            dni = input("DNI del paciente: ")
            fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ")
            paciente = Paciente(nombre, dni, fecha_nac)
            self.clinica.agregar_paciente(paciente)
            print("Paciente agregado con éxito.")
        except Exception as e:
            print(f"Error: {e}")
    def agregar_medico(self):
        try:
            nombre = input("Nombre del médico: ")
            matricula = input("Matrícula del médico: ")
            medico = Medico(nombre, matricula)
            self.clinica.agregar_medico(medico)
            print("Médico agregado con éxito.")
        except Exception as e:
            print(f"Error: {e}")
    def agendar_turno(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            especialidad = input("Especialidad: ")
            fecha_str = input("Fecha y hora (formato: dd/mm/aaaa hh:mm): ")
            fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")

            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado con éxito.")
        except Exception as e:
            print(f"Error: {e}")
    def agregar_especialidad(self):
        try:
            matricula = input("Matrícula del médico: ")
            tipo = input("Nombre de la especialidad: ")
            dias = input("Días de atención (separados por coma, ej: lunes,martes): ").split(",")
            dias = [d.strip().lower() for d in dias]
            especialidad = Especialidad(tipo, dias)

            medico = self.clinica.obtener_medico_por_matricula(matricula)
            medico.agregar_especialidad(especialidad)
            print("Especialidad agregada al médico.")
        except Exception as e:
            print(f"Error: {e}")
    def emitir_receta(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            medicamentos = input("Medicamentos (separados por coma): ").split(",")
            medicamentos = [m.strip() for m in medicamentos if m.strip()]
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida con éxito.")
        except Exception as e:
            print(f"Error: {e}")
    def ver_historia_clinica(self):
        try:
            dni = input("DNI del paciente: ")
            historia = self.clinica.obtener_historia_clinica_por_dni(dni)
            print(historia)
        except Exception as e:
            print(f"Error: {e}")
    def ver_turnos(self):
        turnos = self.clinica.obtener_turnos()
        if turnos:
            for t in turnos:
                print(t)
        else:
            print("No hay turnos registrados.")

    def ver_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        if pacientes:
            for p in pacientes:
                print(p)
        else:
            print("No hay pacientes registrados.")

    def ver_medicos(self):
        medicos = self.clinica.obtener_medicos()
        if medicos:
            for m in medicos:
                print(m)
        else:
            print("No hay médicos registrados.")
    def ver_turnos(self):
        turnos = self.clinica.obtener_turnos()
        if turnos:
            for t in turnos:
                print(t)
        else:
            print("No hay turnos registrados.")

    def ver_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        if pacientes:
            for p in pacientes:
                print(p)
        else:
            print("No hay pacientes registrados.")

    def ver_medicos(self):
        medicos = self.clinica.obtener_medicos()
        if medicos:
            for m in medicos:
                print(m)
        else:
            print("No hay médicos registrados.")
