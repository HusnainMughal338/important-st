import streamlit as st
st.image("https://eu-images.contentstack.com/v3/assets/blt6b0f74e5591baa03/blt7c0bf7e21d4410b4/6319700b8cc2fa14e223aa27/8895.png?width=1280&auto=webp&quality=95&format=jpg&disable=upscale")

st.header("In streamlit show graph.")
st.code(
    'import streamlit as st'
)
st.code(
    'import pandas as pd'
)
st.code(
    'import numpy as np'
)
st.code(
    "df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])"
)
st.code(
    "st.line_chart(df)"
)
st.image("https://images.datacamp.com/image/upload/v1640050215/image15_fgtbqf.png")