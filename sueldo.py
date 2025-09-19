"""
Akemi Clarissa Olvera Arao
19/09/25
Calcular el sueldo semanal de un empleado
"""


# Declaraciones


# Entradas
horas = float(input("Horas trabajadas esta semana: "))
tarifa = float(input("Tarifa horaria: "))
horas_extras = 0

# Proceso
if horas > 48:
    horas_extras = horas - 48
    horas = 48
pago_extra = horas_extras * tarifa * 2
sueldo = horas * tarifa + pago_extra

# Salidas
print("Horas extras: ", horas_extras)
print("Sueldo por horas extras: $", pago_extra)
print("Sueldo total: $", sueldo)
