#Una empresa que comercializa cosméticos tiene organizados a sus vendedores en tres departamentos y ha establecido un programa de incentivos para incrementar su productividad. El gerente, al final del mes, pide el importe global de las ventas de los tres departamentos y aquellos que excedan el 33% de las ventas totales se les paga una cantidad extra equivalente al 20% de su salario bruto mensual.  Si todos los vendedores ganan lo mismo, determinar cuánto recibirán los vendedores de los tres departamentos al finalizar el mes.

def calcular_incentivos(ventas_departamentos, salario_mensual):
    ventas_totales = sum(ventas_departamentos)
    incentivo = 0.20 * salario_mensual
    pagos = [salario_mensual] * 3
    
    for i, ventas in enumerate(ventas_departamentos):
        if ventas > 0.33 * ventas_totales:
            pagos[i] += incentivo
    
    return pagos

ventas_departamento1 = float(input("Ingrese las ventas del Departamento 1: "))
ventas_departamento2 = float(input("Ingrese las ventas del Departamento 2: "))
ventas_departamento3 = float(input("Ingrese las ventas del Departamento 3: "))

salario_mensual = float(input("Ingrese el salario mensual de los vendedores: "))

ventas_departamentos = [ventas_departamento1, ventas_departamento2, ventas_departamento3]
pagos = calcular_incentivos(ventas_departamentos, salario_mensual)

for i, pago in enumerate(pagos, 1):
    print(f"El pago total para los vendedores del Departamento {i} es: {pago:.2f} COP")
