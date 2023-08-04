import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np



st.write('# Youtube View')
image = Image.open('test.gif')
st.image(image, caption='이거보여주려고 어로끌었다')
st.write('## TEST View')
view2 = {
    'str1':[2,4,5,7,8,2,5,6,1,4,6],
    'str2':[1,3,5,2,3,2,5,8,1,4,5],
    'str3':[6,4,5,7,5,4,5,3,1,2,6],
    'str4':[5,2,5,3,9,2,5,6,1,4,4],
}
view2
st.line_chart(view2)
sview2 = pd.Series(view2)
sview2

st.write('## raw')
view = {'1m':100, '2m':150, '3m':30, '4m':145, '5m':23, '6m':45, '7m':76, '8m':90, '9m':127, '10m':100, '11m':124, '12m':60}
view

st.write('## bar chartyyyyyy')
st.area_chart(view)

sview = pd.Series(view)
sview

st.write('## chart_data')
chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['a', 'b', 'c', 'd'])
st.bar_chart(chart_data)