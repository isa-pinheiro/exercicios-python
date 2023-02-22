import urllib.request

try:
    site = urllib.request.urlopen('http://spotify.com.br')
except:
    print('o site nao pode ser acessado')
else:
    print('o site foi acessado')