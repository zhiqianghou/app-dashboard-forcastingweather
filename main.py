import streamlit as st
import plotly.express as px
from back_end import get_data


st.title("Weather Forecast for the next Days")
place = st.text_input("Place:")
days = st.slider("Forcast Days:", min_value=1, max_value= 5,
				 help="Select the number of forecasted days")
option = st.selectbox("Select data type to view",
					  ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

data = get_data()
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y":"Temperater(C)"})

st.plotly_chart(figure)






