altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f"Seu imc é {imc}. Você está abaixo do peso, procure um especialista.")

elif 18.5 <= imc < 25:
    print(f"Parabéns, seu imc é {imc}. Você está no peso ideal.")

else:
   print(f"Seu imc é {imc}. Você está acima do peso, procure um especialista.")