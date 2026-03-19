real = float(input('quanto dinheiro você tem na carteira? r$:'))
dolar = real/5.36
print('com r${:.2F} você pode comprar us${:.2f}'.format(real, dolar))
