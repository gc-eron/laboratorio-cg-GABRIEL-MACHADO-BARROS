import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 5: HSV e recorte")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)

# 1. HSV
st.header("1. HSV")
col1, col2 = st.columns(2)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
col1.image(img, caption="img")
so_h = hsv.copy()
so_h[:, :, 1] = 255
so_h[:, :, 2] = 255
rgb = cv2.cvtColor(so_h, cv2.COLOR_HSV2RGB)

col2.image(rgb, caption="h")

# 2. Mudando o HSV
st.header("2. Mudando o HSV")
col1, col2, col3 = st.columns(3)

fator = col1.slider("Saturação", 0.0, 2.0, 1.5)
fator_b = col2.slider("Brilho", 0.0, 2.0, 1.5)
s = hsv[:, :, 1].astype(float)
b = hsv[:, :, 2].astype(float)
s = s * fator
b = b * fator_b
s = np.clip(s, 0, 255)
b = np.clip(b, 0, 255)
hsv2 = hsv.copy()
hsv3 = hsv.copy()
hsv2[:, :, 1] = s
hsv3[:, :, 2] = b
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))
col2.image(cv2.cvtColor(hsv3, cv2.COLOR_HSV2RGB))

giro = col3.slider("Giro (graus)", 0, 360, 120)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV).astype(np.int16)
delta_h = giro / 2.0
hsv[:, :, 0] = (hsv[:, :, 0] + delta_h) % 180
hsv = hsv.astype(np.uint8)

resultado_giro = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

col3.image(resultado_giro)