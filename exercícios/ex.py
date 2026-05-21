nome=str(input("qual é o seu nome? "))
if nome == "Gustavo":
    print("que nome bonito")
elif nome == "Paulo" or nome == "Maria" or nome == "Pedro":
    print("Seu nome é bem popular no Brasil")
elif nome in ["Ana", "Claudia", "Jéssica", "Juliana"]:
    print("que belo nome feminino")
else:
    print("seu nome é bem normal")
    print("tenha um bom dia {}".format(nome))
