"""
Akemi Clarissa Olvera Arao
19/09/25
Calcular el sueldo semanal de un empleado
"""


# Declaraciones


# Entradas
horas = int(input("Horas trabajadas esta semana: "))
tarifa = int(input("Tarifa horaria: "))
horas_extras = 0

# Proceso
if horas > 48:
    horas_extras = horas - 48
    horas = 48
pago_extra = horas_extras * tarifa * 2
sueldo = horas * tarifa + pago_extra

# Salidas
print("Este es el sueldo $", sueldo)
print("Trabajó ", horas_extras, " horas extras y esto se le pagó por esas horas extras", pago_extra)
