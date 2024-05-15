import streamlit as st
st.write("クラウド版テストページ")


st.title("streamlit入門")

st.header("第１回")

st.subheader("課題１－１")

st.caption("キャプションテスト")

st.code("""
#1から10までの整数を足し算するプログラム
sum = 0
for i in range(11):
  sum += i
print(sum)""")

st.divider()


if st.button("ボタンです"):
  st.write("ボタンが押されました")

num1 = st.number_input("数字１を入力して",step=1)

num2 = st.number_input("数字２を入力して",step=1)

num=num1+num2
st.write("足し算した結果は"+str(num)+"です")

choice = st.radio("どちらの計算をする？",['足し算','掛け算'])

if choice == "足し算":
  st.write("足し算した結果は",num1 + num2,"です")
elif choice == '掛け算':
  st.write("掛け算した結果は",num1 * num2,"です")


choice1 = st.checkbox("足し算をしたい")
choice2 = st.checkbox("掛け算をしたい")
choice3 = st.checkbox("引き算をしたい")

if choice1:
  st.write("足し算した結果は",num1 + num2,"です")
if choice2:
  st.write("掛け算した結果は",num1 * num2,"です")
if choice3:
  st.write("引き算した結果は",num1 - num2,"です")
