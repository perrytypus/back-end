km = float(input('quantos KM foram percorridos? '))
dias = int(input('quantos dias vc ficou com o carro? '))
pdia = dias*60
pkm = km*0.15
total = pkm + pdia
print('o valor total vai ser de R${}'.format(total))
