def ajuda(parametro):
    return help(parametro)

while True:
    comando = str((input('Insira o comando que voce precisa de ajuda: '))).lower().strip()
    if comando == 'fim':
        break
    else:
        ajuda(comando)