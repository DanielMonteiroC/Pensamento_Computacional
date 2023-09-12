nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))

media = (nota_1 + nota_2)/2

print(media)

if media >= 7:
    print(f"A média é: {media}. Aprovado.")

else:
    print(f"A média é: {media}. Reprovado.")


