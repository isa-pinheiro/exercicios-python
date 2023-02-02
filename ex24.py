#se nao começar com santo, o programa retorna false
city = input('Digite a cidade que você nasceu: ').strip().lower()
print(city[:5] == 'santo')