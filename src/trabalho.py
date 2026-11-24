import cv2
import numpy as np
import streamlit as st
from PIL import Image, ImageOps

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

st.header("1. Saturação")

fator_saturacao = st.slider("Saturação", 0.0, 2.0, 1.0, step=0.05)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV).astype(np.float32)
hsv[:, :, 1] = np.clip(hsv[:, :, 1] * fator_saturacao, 0, 255)
hsv = hsv.astype(np.uint8)

resultado_saturacao = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

col1, col2 = st.columns(2)
col1.image(img, caption="Original")
col2.image(resultado_saturacao, caption="Resultado da Saturação")

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

st.header("2. Brilho")

fator_brilho = st.slider("Brilho", 0.0, 2.0, 1.0, step=0.05)

hsv_brilho = cv2.cvtColor(img, cv2.COLOR_RGB2HSV).astype(np.float32)
hsv_brilho[:, :, 2] = np.clip(hsv[:, :, 2] * fator_brilho, 0, 255)
hsv_brilho = hsv_brilho.astype(np.uint8)

resultadoBrilho = cv2.cvtColor(hsv_brilho, cv2.COLOR_HSV2RGB)

col1, col2 = st.columns(2)
col1.image(foto, caption="Original")
col2.image(resultadoBrilho, caption="Resultado do Brilho")

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

st.header("8. Negativo")

foto_negativa = ImageOps.invert(foto)
col1, col2 = st.columns(2)
col1.image(foto, caption="Original")
col2.image(foto_negativa, caption="Cores invertidas")

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

st.header("9. Recorte")

h, w = img.shape[:2]
max = min(h, w)

lado = st.slider("Tamanho do recorte", 10, max-1, min(200, max))
x = st.slider("x", 0, w - lado, 0)
y = st.slider("y", 0, h - lado, 0)

corte = img[y : y + lado, x : x + lado]

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(corte, caption="Recorte")

with col3:
    st.write(' ')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

st.header("11. Espelhamento")

foto_espelhada = ImageOps.mirror(foto)
foto_espelhada = ImageOps.flip(foto_espelhada)

col1, col2 = st.columns(2)
col1.image(foto, caption="Original")
col2.image(foto_espelhada, caption="Espelhamento (horizontal e vertical)")
