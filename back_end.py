import requests

API_KEY = "752de33972b43233c2782a87d5aabc23"


def get_data(place, num_of_days=None):
	url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
	response = requests.get(url)
	data = response.json()
	filtered_data = data["list"]
	num_values = 8 * num_of_days
	filtered_data = filtered_data[:num_values]

	return filtered_data


if __name__ == "__main__":
	print(get_data(place="Dallas", num_of_days=3))



