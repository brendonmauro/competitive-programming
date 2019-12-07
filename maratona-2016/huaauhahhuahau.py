stri = input()
vogais = ['a','e','i','o','u']
palin = ''
novaStri = ''

for letra in stri:
	if letra in vogais:
		novaStri += letra;

for i in range(len(novaStri)-1,-1,-1):
	palin += novaStri[i]

if palin == novaStri:
	print('S')
else:
	print('N')