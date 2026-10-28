import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Imagem como matriz")

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:] = (206, 43, 55)
bandeira[:, :6] = (0, 146, 70)
bandeira[:, 6:12] = (241, 242, 241)
st.image(ampliar(bandeira))

"Bandeira da Itália"