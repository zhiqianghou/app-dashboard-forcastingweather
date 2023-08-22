import streamlit as st
import plotly.express as px


st.title("Weather Forecast for the next Days")
place = st.text_input("Place:")
days = st.slider("Forcast Days:", min_value=1, max_value= 5,
				 help="Select the number of forecasted days")
option = st.selectbox("Select data type to view",
					  ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2023-08-01", "2023-08-02", "2023-08-03"]
temperatures = [10, 20, 30]
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y":"Temperater(C)"})

st.plotly_chart(figure)






