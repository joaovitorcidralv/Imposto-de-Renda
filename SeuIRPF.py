print('\033[0;33m=-\033[0;33m' * 35)
print(' ')
print('\033[1;33m                     CALCULADORA DE IMPOSTO DE RENDA\033[1;33m')
print(' ')
print('\033[0;33m=-\033[0;33m' * 35)
NumDepend = int(input("Informe o número de dependentes: "))
SalarioBruto = float(input("Informe o salário bruto: "))

def calcular_aliquota_inss(salario_bruto):
    switch = {
        salario_bruto < 1045.00: 0.075,
        salario_bruto < 2089.60: 0.09,
        salario_bruto < 3134.40: 0.12,
        True: 0.14
    }
    return switch.get(True)

AliquotaINSS = calcular_aliquota_inss(SalarioBruto)

BaseCalculoIRPF = SalarioBruto - (AliquotaINSS * SalarioBruto) - (189.59 * NumDepend)

def calcular_aliquota_irpf(base_calculo):
    switch = {
        base_calculo < 1903.98: (0, 0),
        base_calculo < 2826.65: (0.075, 142.80),
        base_calculo < 3751.05: (0.15, 354.80),
        base_calculo < 4664.68: (0.225, 636.13),
        True: (0.275, 869.36)
    }
    return switch.get(True)

AliquotaIRPF, parcela_dedutivel = calcular_aliquota_irpf(BaseCalculoIRPF)
ValorIRPF = (BaseCalculoIRPF * AliquotaIRPF) - parcela_dedutivel

ValorMensalIRPF = ValorIRPF / 12

print(f'Você pagará {ValorMensalIRPF:.2f} de Imposto de Renda por mês.')