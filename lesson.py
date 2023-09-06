import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.write('ファイル更新テスト')


#lesson7プログレスバー
st.write('lesson7:プログレスバー')
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


#lesson6レイアウト
st.sidebar.write('lesson6:レイアウト(サイドバー)')
text2=st.sidebar.text_input('あなたの職業は？',key='text2')
condition2=st.sidebar.slider('あなたの年齢は？',0,100,50,key='condition2') #最小値、最大値、デフォルト値

st.write('lesson6:レイアウト(サイドバー)')
'あなたの職業',text2
'年齢',condition2


st.write('lesson6:レイアウト(2カラム)')
left_column,right_column = st.columns(2)

button=left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')


st.write('lesson6:レイアウト(エクスパンダー)')
expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の回答')


#lesson5インタラクティブなウィジェット
st.write('lesson5:インタラクティブなウィジェット(テキストボックス)')
text=st.text_input('あなたの趣味は？')
'あなたの趣味',text


st.write('lesson5:インタラクティブなウィジェット（スライダー）')
condition=st.slider('あなたの調子は？',0,100,50) #最小値、最大値、デフォルト値
'コンディション',condition



#lesson4画像の表示
st.write('lesson4:画像の表示')
img=Image.open('sample.jpg')
st.image(img,caption='画像表示のサンプルです',use_column_width=True)

#lesson3グラフとマップの表示
df2=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.write('lesson3:line_chartで折れ線グラフの表示')
st.line_chart(df2)

df3=pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)

st.write('地図の表示')
st.map(df3)


#lesson2マークダウン記法での表示
"""
# lesson2マークダウン記法での表示
## 節
### 項
"""

st.write('プログラムの内容もマークダウンで書ける。コピペも簡単')
"""
```python

import streamlit as st
import pandas as pd
```
"""




#lesson1タイトルと単純な文字列とデータフレームの表示
st.title("lesson1:Streamlitでタイトルを表示！")

st.write('DataFrame')

df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#writeでデータフレーム表示
st.write('st.write(df)')
st.write(df)

#dataframeでデータフレーム表示
st.write('st.dataframe(df)')
st.dataframe(df)

#dataframeだと幅と高さを指定して表示できる
st.write('st.dataframe(df,width=100,height=100)')
st.dataframe(df,width=100,height=100)


#df.style.highlight_max()を使うと最大の値を強調表示できる
st.write('st.dataframe(df.style.highlight_max(axis=0),width=150,height=150)')
st.dataframe(df.style.highlight_max(axis=0),width=150,height=150)

#tableでデータフレーム表示
st.write('st.table(df)')
st.table(df)
