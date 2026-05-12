velocidade=float(input("Qual a velocidade do carro? "))
if velocidade > 80:
    limite=velocidade - 80
    multa=limite * 7
    print(f" você foi multado!")
    print(f"O valor da multa é R${multa:.2f}")
else:
    print("Velocidade dentro do limite")
