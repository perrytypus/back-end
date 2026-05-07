num = int(input("digite um numero enre 0 e 9999 "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f"unidade {unidade}")
print(f"dezena {dezena}")
print(f"cenena {centena}")
print(f"milhar {milhar}")
