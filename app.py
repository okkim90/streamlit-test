import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np



st.write('# 악으로깡 으로버 텨라 ')
image = Image.open('test.gif')
st.image(image, caption='이거보여주려고 어로끌었다')
st.write('## 미안하다 이거 보여주려고 어그로끌었다.. 나루토 사스케 싸움수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 싸움이다.. 그찐따같던 나루토가 맞나?')
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

st.write('## 너무 감격스럽고 모두어엿하게 큰거보니 내가 다 뭔가 알수없는 추억이라')
view = {'1m':100, '2m':150, '3m':30, '4m':145, '5m':23, '6m':45, '7m':76, '8m':90, '9m':127, '10m':100, '11m':124, '12m':60}
view

st.write('## 루토그라서 계속보는중인데 저거 ㄹㅇ이냐..? 하.. ㅆㅂ 사스케 보고싶다..  진짜언제 이렇게 신급 최강들이 되었을까 옛날생각나고 나 중딩때생각나고 뭔가 슬프기도하고 좋기도하고 감격도하고 여러가지감정이 복잡')
st.area_chart(view)

sview = pd.Series(view)
sview

st.write('## 무튼 나루토는 진짜 애니중최거명작')
chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['a', 'b', 'c', 'd'])
st.bar_chart(chart_data)