"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd


with st.echo(code_location="above")
    df = pd.DataFrame({
      'first column': [1, 2, 3, 4],
      'second column': [10, 20, 30, 40]
    })

    df

    st.table(df)
