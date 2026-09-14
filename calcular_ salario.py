def calcular_salario(horas, pago_por_hora):
    salario = horas * pago_por_hora
    return salario

if __name__ == "__main__":
    horas = 40
    pago_por_hora = 8.5
    resultado = calcular_salario(horas, pago_por_hora)
    print("Las horas trabajadas son:", horas)
    print("El pago por hora es: $", pago_por_hora)
    print("El salario semanal es: $", resultado)
