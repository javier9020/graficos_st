# dia 5
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Ejemplo 1

st.write('Hello, *World!* :sunglasses:')

# Ejemplo 2

st.write(1234)

# Ejemplo 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })


st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Ejemplo 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['x', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(alt.X('x').title('Eje x'), y='b', size='c', color='c', tooltip=['x', 'b', 'c'])
st.write(c)
