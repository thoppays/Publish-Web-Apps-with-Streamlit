import streamlit as st
import pandas

data = {
  "Series 1": [1, 2, 3, 4, 5, 6],
  "Series 2": [100, 200, 300, 400, 700, 1500]
}

df = pandas.DataFrame(data)

st.title("My First Streamlit App")
st.subheader("Introducing Streamlit App")
st.write("""This is my first web app
Enjoy it!!!""")
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider("Celsius")
st.write(myslider, "in Fahrenheit is", myslider*9/5+32)