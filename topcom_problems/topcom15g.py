texto = ""

while True:
  try:
    entrada = input() + "\n"
    texto += entrada
  except EOFError:
    break

texto = texto[:len(texto)-1]
novoTxt = ""
carac = ""
for letra in texto:
  if str.isnumeric(letra) or letra in "()":
    carac += letra
  else:
    novoTxt += letra
    carac = ""
    continue
  if len(carac) == 3:
    if carac[0] == '(':
      novoTxt += carac[1]
    else:
      novoTxt += chr(int(carac))
    carac = ""
print(novoTxt, end="")