import streamlit as st
import plotly.express as px
from back_end import get_data

#Add title, text input, slider, selectbox, subheader
st.title("Weather Forecast for the next Days")
place = st.text_input("Place:")
days = st.slider("Forcast Days:", min_value=1, max_value= 5,
				 help="Select the number of forecasted days")
option = st.selectbox("Select data type to view",
					  ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Get the temperature/Sky data
filtered_data = get_data(place, days)

if place:
	#Visualization of the forecasting temperature
	if option == "Temperature":
		temperatures = [dict['main']['temp'] for dict in filtered_data]
		dates = [dict["dt_txt"] for dict in filtered_data]
		figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y":"Temperater(C)"})
		st.plotly_chart(figure)

	# Visualization of the sky data
	if option == "Sky":
		images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
				  "Rain": "images/rain", "Snow":"images/snow"}
		sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
		image_path = [images[condition] for condition in sky_conditions]
		st.image(image_path, width=110)







