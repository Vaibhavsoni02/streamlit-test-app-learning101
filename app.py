"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np

with st.echo(code_location="above"):
    df = pd.DataFrame({
      'first column': [1, 2, 3, 4],
      'second column': [10, 20, 30, 40]
    })

    df

    
    
with st.echo(code_location="above"):    
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

with st.echo(code_location="above"):    
    dataframe = np.random.randn(10, 20)
    st.dataframe(dataframe)
    
    
with st.echo(code_location="above"):  
    dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

    st.dataframe(dataframe.style.highlight_max(axis=0))
