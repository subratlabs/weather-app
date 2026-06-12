import tkinter as tk
# for making gui apps for windows button and labels

import requests
# to connect internet and fetch weather


# api key
API_key = "YOUR_API_KEY"
# it allows your app to acess weather data

# function to get weather
def get_weather():    # this function is run when button clicked

    city = city_entry.get()
    # takes city name typed by user from input box

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"

    response = requests.get(url)
    #  python send request to weather app

    if response.status_code == 200:
        # 200 means everything works correctly

        data = response.json()
        # converts api data into pyrhon dictionary format

        weather = data["weather"][0]["description"]
        # gets weather condition

        temp = data["main"]["temp"]   # for temperature
        feels = data["main"]["feels_like"]   # get deels like temperature
        humidity = data["main"]["humidity"]   # gets humidity
        wind_speed = data["wind"]["speed"]    # gets wind speed
        country = data["sys"]["country"]     #gets country code


        result_label.config(    # changes text inside result label dynamically
            # allows variables insidee text
            text=f"""  
City: {city}, {country}
Weather: {weather}
Temperature: {temp}℃
Feels Like: {feels}℃
Wind Speed: {wind_speed}m/s
Humidity: {humidity}%
"""            
        )

    else:    # if apis fails city not found
        result_label.config(text="City not found")
        # shows error message on screen

# main window
root = tk.Tk()
# creates app window

root.title("Weather App")
# sets app name or title

root.geometry("400x400")
# width and heigth


title = tk.Label(root, text="Weather App", font=("Arial", 20))
# creates heading text

title.pack(pady=10)
# places heading on screens

# input box

city_entry = tk.Entry(root, font=("Arial", 14))
# create typing box for city name

city_entry.pack(pady=10)
# please input box on screen

# BUTTON

search_button = tk.Button(root, text="Get Weather", command=get_weather)
# create button and when clicked rub=ns get_weather() finction

search_button.pack(pady=10)
# places button o screen

#result label
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
# creates lable to display weather results and justify left means text alings left side

result_label.pack(pady=20)
# places result label on screen

# run app
root.mainloop()
# keeps app window running forever