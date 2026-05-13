ano=int(input('digite um ano pra saber se ele é bissexto '))
if (ano %4==0 and ano %100!=0) or (ano%400==0):
    print(f'O ano {ano} é bisexto')
else:
    print(f'O ano {ano} não é bissexto')
