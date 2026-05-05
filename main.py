with open("notas.txt", "a") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo guardado no arquivo:")
    print(conteudo)