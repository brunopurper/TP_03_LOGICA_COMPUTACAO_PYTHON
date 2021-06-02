idade = int(input("Informe a sua idade: "))

if idade < 1:
    print("Idade inválida, tente novamente")
    exit()

if idade >= 18 and idade <= 69 :
    print("Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)")
elif idade >= 16 and idade < 18 or idade >= 70:
    print("Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).")
else:
    print("Não tem direito a voto (menor de 16 anos).")