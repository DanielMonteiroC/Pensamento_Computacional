temp = eval(input('Digite a temperatura atual: '))

if temp > 86:
    print('Está quente!\nTome bastante líquido.')

elif temp > 32:
    print('Está frio!')

else:
    print('Está Congelando!\nTraga uma jaqueta.')

print('Adeus.')
