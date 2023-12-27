

def calculoPreco(valor,quantidade):
    total = valor * quantidade
    print(f"O custo total da compra sera: \n R$: {str(round(total,2)).replace('.',',')}")

print(" ----- FEIRA DAS MAÇAS ------- ")
print("\nTabela de Preços das Maças:\n")
print("\t- R$ 1,30 por menos de 1 dúzia \n \t- R$ 1,00 por mais ou igual 1 duzia\n")

quantidade_macas = int(input("Digite quantas maças deseja comprar: "))

print()
if quantidade_macas < 12:
    calculoPreco(1.30,quantidade_macas)
else:
    calculoPreco(1.00,quantidade_macas)
print()