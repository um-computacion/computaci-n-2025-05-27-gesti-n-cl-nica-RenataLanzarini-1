class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        if not tipo.strip():
            raise ValueError("El tipo de especialidad no puede estar vacío.")
        if not all(dia.isalpha() for dia in dias):
            raise ValueError("Los días deben ser palabras (ej: lunes, martes).")

        self.__tipo = tipo
        self.__dias = [dia.lower() for dia in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"
