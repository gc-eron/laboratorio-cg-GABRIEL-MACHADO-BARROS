import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Padrão")

k = st.slider("k", 1, 20, 4)
y, x = np.indices((64, 64))
def padrao(x, k):
    return (x * k) % 256

def padrao2(x, y, k):
    return ((x + y) * k) % 256

def padrao3(x, y, k):
    return ((x ^ y) * k) % 256

def padrao4(x, y, k):
    return (((x-32)**2 + (y-32)**2) * k // 4) % 256

def padrao5(x, y, k):
    return ((x + 2 * y) * k) % 256

def padrao6(x, y, k):
    return ((x ** 2) * k) % 256


#imagem = padrao(x, y, k).astype(np.uint8)
#st.image(ampliar(imagem, 4))

#imagem2 = padrao2(x, y, k).astype(np.uint8)
#st.image(ampliar(imagem2, 4))

#imagem3 = padrao3(x, y, k).astype(np.uint8)
#st.image(ampliar(imagem3, 4))

imagem4 = padrao4(x, y, k).astype(np.uint8)
st.image(ampliar(imagem4, 4))


#imagem5 = padrao5(x, y, k).astype(np.uint8)
#st.image(ampliar(imagem5, 4))

#imagem6 = padrao6(x, y, k).astype(np.uint8)
#st.image(ampliar(imagem6, 4))
