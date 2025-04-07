for i in range(0, 256):
    print(f"{i} = {chr(i)}")
    if i % 20 == 0 and i != 0:
        input("Continuar? (Enter)")
