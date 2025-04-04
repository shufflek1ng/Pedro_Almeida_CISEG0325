compra=0
desconto=0

cliente=(input("Digite o seu nome: "))

compra=float(input("Qual é o valor da compra? : € "))

if compra <= 200:
    print(f"{cliente} a sua compra no valor de {compra}€ tem um desconto de 10% no valor de {compra - (compra * 0.10)}€")
elif compra > 200 and compra <= 500:
    print(f"{cliente} a sua compra no valor de {compra}€ tem um desconto de 15% no valor de {compra - (compra * 0.15)}€")
else:
    print(f"{cliente} a sua compra no valor de {compra}€ tem um desconto de 20% no valor de {compra - (compra * 0.20)}€")
