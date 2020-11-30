import streamlit as st
import pandas as pd
import numpy as np

a = st.file_uploader(label='Multiple Reruns', accept_multiple_files=True)
st.write(a)


st.markdown('### Testing for Re-runs')
st.write('Here is a random dataframe. With every re-run the numbers in the dataframe should update')
df = pd.DataFrame(np.random.randint(0, 10, size=(5, 2)), columns=list('AB'))
st.write(df)
