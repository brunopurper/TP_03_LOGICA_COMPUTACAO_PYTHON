
consumo = float(input("Informe o valor total do consumo: "))
total_pessoas = int(input("Informe o total de pessoas: "))
percentual = int(input("Informe a taxa de serviço: "))

if total_pessoas < 1:
    print("O número de pessoas não pode ser menor do que 0.")
    exit()
if percentual > 100:
    print("O percentual não pode ser maior do que 100.")
    exit()


def total(consumo, total_pessoas, percentual):
    percentual = percentual / 100
    total = (consumo * percentual + consumo) / total_pessoas
    total = str(total).replace('.',',')
    return total
    

print(f"O valor total da conta, com a taxa de serviço, será de R$: {((consumo * percentual / 100) + consumo)}.")
print(f"Dividindo a conta por {total_pessoas}, cada pessoa deverá pagar R$: {total(consumo, total_pessoas, percentual)}.")

