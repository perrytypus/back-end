distancia=float(input("qual é a distância da viagem? "))
if distancia<=200:
    preco=distancia*0.50
else:
    preco=distancia*0.45
print(f"o preço da sua passagem será R${preco:.2f}")
