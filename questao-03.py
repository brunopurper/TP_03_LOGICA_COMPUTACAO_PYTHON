for contador in range(5):
    participante = input(f"Informe o nome do {contador + 1}° particpante: ")
    nota = float(input(f"Informe a nota do {contador + 1}° particpante: "))

    if contador == 0 or nota > nota_vencedor:
        participante_vencedor = participante    
        nota_vencedor = nota
 

print(f"O vencedor é {participante_vencedor} com a nota de {nota_vencedor}")