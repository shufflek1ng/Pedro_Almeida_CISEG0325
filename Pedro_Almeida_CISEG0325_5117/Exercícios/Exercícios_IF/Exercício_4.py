saldo_inicial=0
cheque=0

saldo_inicial=float(input("Digite o valor do saldo do cliente: € "))

cheque=float(input("Digite o valor do cheque a descontar: € "))

if cheque > saldo_inicial:
    print(f"O saldo não cobre o valor de {cheque:.2f} do cheque.")
else:
    print(f"{cheque:.2f} descontado com sucesso. Saldo restante: € {saldo_inicial - cheque:.2f} ")
