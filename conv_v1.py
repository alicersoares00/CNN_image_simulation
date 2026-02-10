from PIL import Image
from IPython.display import display

#Divisão em tiras verticais e display da imagem original
img = Image.open("teste_pil.jpg")
largura, altura = img.size
print(largura, altura)
display(img)

cols = 20
tiras = []
cortes = []

for i in range(cols):
  left = round(i*largura/cols)
  right = round((i+1)*largura/ cols)
  corte = (left,0,right,altura)
  cortes.append(corte)
  imgc = img.crop(corte)
  tiras.append(imgc)

#Separações e recombinação — Separar tiras em pares e ímpares:
tiras_pares = []
tiras_impares = []

for posicao, tira in enumerate(tiras, start=1):  # começa em 1
    if posicao % 2 == 0:
        tiras_pares.append(tira)     # posições 2,4,6,...
    else:
        tiras_impares.append(tira)   # posições 1,3,5,...

#concatenar tiras pares e concatenar tiras ímpares

#PARES
largura_totalp = sum(t.width for t in tiras_pares)
altura_finalp  = tiras_pares[0].height
modop = tiras_pares[0].mode
novap = Image.new(modop, (largura_totalp, altura_finalp))
x_atual = 0
for tira in tiras_pares:
    novap.paste(tira, (x_atual, 0))
    x_atual += tira.width

display(novap)

#IMPARES
largura_totali = sum(t.width for t in tiras_impares)
altura_finali  = tiras_impares[0].height
modoi = tiras_impares[0].mode
novai = Image.new(modoi, (largura_totali, altura_finali))
x_atual = 0
for tira in tiras_impares:
    novai.paste(tira, (x_atual, 0))
    x_atual += tira.width

display(novai)

#salvando as concatenações
novap.save("impresas_concatenadasPAR.jpg", quality=95)
novai.save("impresas_concatenadasIMPAR.jpg", quality=95)


# Padroniza o modo para evitar incompatibilidades (opcional, mas recomendado)
modo_final = "RGBA" if (novai.mode == "RGBA" or novap.mode == "RGBA") else "RGB"

# Converte se necessário
img_left  = novai.convert(modo_final)  # ímpares à esquerda
img_right = novap.convert(modo_final)  # pares à direita

largura_final = img_left.width + img_right.width
altura_final  = max(img_left.height, img_right.height)
final = Image.new(modo_final, (largura_final, altura_final))
final.paste(img_left,  (0, 0))
final.paste(img_right, (img_left.width, 0))

display(final)
final.save("impresas_concatenadasFINAL.jpg", quality=95)

img = Image.open("impresas_concatenadasFINAL.jpg")
largura, altura = img.size


#cortes horizontais!
rows = 20
tirash = []
cortesh = []

for i in range(rows):
    upper = (i * altura) // rows
    lower = ((i + 1) * altura) // rows if i < rows - 1 else altura
    corteh = (0, upper, largura, lower)
    cortesh.append(corteh)
    imgch = img.crop(corteh)
    tirash.append(imgch)

for k in range(len(tirash)):
    display(tirash[k])

tiras_paresh = []
tiras_imparesh = []

for posicao, tira in enumerate(tirash, start=1):  # começa em 1
    if posicao % 2 == 0:
        tiras_paresh.append(tira)     # posições 2,4,6,...
    else:
        tiras_imparesh.append(tira)   # posições 1,3,5,...

for tira in tiras_imparesh:
  display(tira)
for tira in tiras_paresh:
  display(tira)

#agora preciso dar o concat das paresh e imparesh

largura_impar = max(t.width for t in tiras_imparesh)
altura_impar  = sum(t.height for t in tiras_imparesh)
modo_impar = tiras_imparesh[0].mode

img_impares = Image.new(modo_impar, (largura_impar, altura_impar))
y = 0
for t in tiras_imparesh:
    img_impares.paste(t, (0, y))
    y += t.height

display(img_impares)
img_impares.save("linhas_impares.png")

largura_par = max(t.width for t in tiras_paresh)
altura_par  = sum(t.height for t in tiras_paresh)
modo_par    = tiras_paresh[0].mode

img_pares = Image.new(modo_par, (largura_par, altura_par))
y = 0
for t in tiras_paresh:
    img_pares.paste(t, (0, y))
    y += t.height

display(img_pares)
img_pares.save("linhas_pares.png")

