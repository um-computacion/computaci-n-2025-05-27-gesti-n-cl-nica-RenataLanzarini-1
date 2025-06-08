import unittest
from datetime import datetime

from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import *

class TestClinica(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()

        # Paciente
        self.paciente = Paciente("Juan Pérez", "11111111", "12/12/2000")
        self.clinica.agregar_paciente(self.paciente)

        # Médico con especialidad en lunes
        self.medico = Medico("Dra. García", "22222")
        especialidad = Especialidad("Pediatría", ["lunes"])
        self.medico.agregar_especialidad(especialidad)
        self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_valido(self):
        fecha = datetime(2025, 6, 9, 10, 0)  # lunes
        self.clinica.agendar_turno("11111111", "22222", "Pediatría", fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "22222")

    def test_turno_medico_no_disponible(self):
        fecha = datetime(2025, 6, 11, 10, 0)  # miércoles (no trabaja)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("11111111", "22222", "Pediatría", fecha)

    def test_turno_especialidad_incorrecta(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("11111111", "22222", "Cardiología", fecha)

    def test_turno_duplicado(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        self.clinica.agendar_turno("11111111", "22222", "Pediatría", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("11111111", "22222", "Pediatría", fecha)

    def test_emitir_receta_valida(self):
        medicamentos = ["Ibuprofeno", "Paracetamol"]
        self.clinica.emitir_receta("11111111", "22222", medicamentos)
        historia = self.clinica.obtener_historia_clinica_por_dni("11111111")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("11111111", "22222", [])

    def test_error_paciente_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "22222", "Pediatría", datetime.now())

    def test_error_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("11111111", "99999", "Pediatría", datetime.now())

if __name__ == "__main__":
    unittest.main()
