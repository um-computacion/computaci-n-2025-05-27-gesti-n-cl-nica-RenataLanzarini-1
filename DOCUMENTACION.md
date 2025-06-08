Documentación del Sistema de Gestión para una Clínica

1. Cómo ejecutar el sistema

Desde la terminal, ubicado en la raíz del proyecto, ejecutar:

```bash
python3 main.py
Esto abrirá un menú por consola con las opciones del sistema:
--- Menú Clínica ---
1) Agregar paciente
2) Agregar médico
3) Agendar turno
4) Agregar especialidad
5) Emitir receta
6) Ver historia clínica
7) Ver todos los turnos
8) Ver todos los pacientes
9) Ver todos los médicos
0) Salir

Detalle de cada opción del menú:

1) Agregar paciente
Pide por consola:

Nombre
DNI (único)
Fecha de nacimiento (formato dd/mm/aaaa)
Luego crea un objeto Paciente y lo registra en la clínica. Si el DNI ya existe, mostrará un mensaje de error.

2) Agregar médico
Solicita:

Nombre completo
Matrícula (clave única)
Crea un objeto Medico y lo guarda. Inicialmente no tiene especialidades asignadas.

3) Agendar turno
Solicita:

DNI del paciente
Matrícula del médico
Especialidad (debe coincidir con alguna que el médico atienda)
Fecha y hora (en formato dd/mm/aaaa hh:mm)

Crea un Turno si se cumplen estas condiciones:

El médico atiende ese día
La especialidad es válida ese día
No hay otro turno agendado en esa fecha/hora

4) Agregar especialidad a un médico
Solicita:

Matrícula del médico
Nombre de la especialidad (ej: Pediatría)
Días de atención (ej: lunes, miércoles)
Agrega una nueva especialidad al médico correspondiente.

5) Emitir receta
Solicita:

DNI del paciente
Matrícula del médico
Lista de medicamentos (separados por coma)
Crea una Receta si existen el paciente y el médico, y al menos un medicamento válido.

6) Ver historia clínica
Pide el DNI del paciente y muestra:

Todos los turnos agendados
Todas las recetas emitidas
El resultado es una representación textual de su HistoriaClinica.

7) Ver todos los turnos
Muestra todos los turnos registrados en el sistema, incluyendo:

Paciente
Médico
Especialidad
Fecha y hora

8) Ver todos los pacientes
Lista todos los pacientes registrados en el sistema, mostrando:

Nombre
DNI
Fecha de nacimiento

9) Ver todos los médicos
Lista todos los médicos con:

Nombre
Matrícula
Especialidades y días de atención

0) Salir
Finaliza la ejecución del programa.

2. Cómo ejecutar las pruebas

Ejecutar todas las pruebas:
python3 -m unittest discover tests

Ejecutar un archivo específico:
python3 -m unittest tests/test_clinica.py

3. Explicación del diseño general
El sistema está organizado en tres módulos principales:

modelo/
Contiene las clases principales:

Paciente, Medico, Especialidad, Turno, Receta, HistoriaClinica, Clinica

Cada clase valida internamente los datos que recibe.

Se definen excepciones personalizadas para representar errores del dominio.

cli/
Contiene la clase InterfazUsuario, que representa la interfaz de consola.

Muestra el menú y captura entrada del usuario.

Llama a métodos del modelo (Clinica) para realizar acciones.

No implementa lógica de negocio, solo interacción.

tests/
Contiene pruebas unitarias usando unittest, incluyendo:

Casos válidos (turnos, recetas, pacientes)

Casos erróneos (duplicados, médicos no disponibles, recetas vacías, etc.)

Verificación de que el sistema respeta reglas de negocio.

