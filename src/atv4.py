import numpy as np
import streamlit as st
from PIL import Image
st.title("Atv 4: RGB")
st.header("1. Leitura da foto")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
col1, col2 = st.columns(2)

col1.image(img)
col2.text(img.shape)
col2.text(img[100, 100])
col2.image(np.full((100, 100, 3), img[100, 100], dtype=np.uint8))


st.header("2. Canais")

col1, col2 = st.columns(2)

uma_escala_r = img[:, :, 0]
uma_escala_g = img[:, :, 1]
uma_escala_b = img[:, :, 2]

col1.image(uma_escala_r, caption="Uma escala R")
col1.image(uma_escala_g, caption="Uma escala G")
col1.image(uma_escala_b, caption="Uma escala B")

so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0
so_g = img.copy()
so_g[:, :, 0] = 0
so_g[:, :, 2] = 0
so_b = img.copy()
so_b[:, :, 0] = 0
so_b[:, :, 1] = 0

col2.image(so_r, caption="Só R")
col2.image(so_g, caption="Só G")
col2.image(so_b, caption="Só B")

st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 255, 0)
col1.image(quadrado, caption="amarelo")
quadrado_vermelho = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado_vermelho[:, :] = (255, 0, 0)
col1.image(quadrado_vermelho, caption="vermelho")
quadrado_verde = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado_verde[:, :] = (0, 255, 0)
col1.image(quadrado_verde, caption="verde")
quadrado_azul = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado_azul[:, :] = (0, 0, 255)
col1.image(quadrado_azul, caption="azul")
col2.image(img, channels="BGR", caption="BGR")

st.header("4. Tons de cinza")
col1, col2 = st.columns(2)
r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
soma = r + g + b
media = (soma / 3).astype(np.uint8)
col1.image(media, caption="média")
soma = 0.299*r + 0.587 * g + 0.114 * b
ponderada = soma.astype(np.uint8)
col2.image(ponderada, caption="ponderada")