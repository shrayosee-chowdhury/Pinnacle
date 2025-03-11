

import tkinter as tk
from tkinter import ttk
import requests

def get_data():
    city = city_name.get()
    
    if not city:
        weather_climate_result.config(text="Select a city!", fg="red")
        return

    try:
        api_key = "5b0355531f75378118503fbd552db2ad"  
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        data = requests.get(url).json()
        
        if data["cod"] != 200:  
            weather_climate_result.config(text="Invalid City!", fg="red")
            return
        
        weather_climate_result.config(text=data["weather"][0]["main"], fg="black")
        weather_description_result.config(text=data["weather"][0]["description"], fg="black")
        temp_result.config(text=f"{data['main']['temp'] - 273.15:.2f}°C", fg="black")
        pre_result.config(text=data["main"]["pressure"], fg="black")
    
    except Exception as e:
        weather_climate_result.config(text="Error!", fg="red")
        print("Error fetching data:", e)

root = tk.Tk()
root.title("Weather App")
root.geometry("500x500")
root.config(bg="deep sky blue")


display_weather = tk.Label(root, text="Weather App", font=("calibri", 30, "bold"), bg="white")
display_weather.place(x=25, y=50, height=50, width=450)

# City Selection
city_name = tk.StringVar()
city_list = [
    "New Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore", "Hyderabad",
    "Ahmedabad", "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Visakhapatnam",
    "Bhopal", "Patna", "Ludhiana", "Agra", "Nashik", "Meerut", "Rajkot"
]

search_location = tk.Label(root, text="Select City:", font=("Times New Roman", 15), bg="deep sky blue")
search_location.place(x=25, y=120)

combo_box = ttk.Combobox(root, values=city_list, font=("calibri", 15, "bold"), textvariable=city_name)
combo_box.place(x=180, y=120, height=40, width=295)

# Search Button
button = tk.Button(root, text="Get Weather", activebackground="silver", bg="black", fg="white",
                   font=("Arial", 12), command=get_data)
button.place(x=200, y=190, height=30, width=100)


labels = ["Weather Climate", "Weather Description", "Temperature", "Pressure"]
y_positions = [255, 325, 395, 465]
results = []

for i, label in enumerate(labels):
    tk.Label(root, text=label, font=("Courier New", 10), bg="white").place(x=25, y=y_positions[i], height=35, width=200)
    result_label = tk.Label(root, text="", font=("Courier New", 10), bg="white")
    result_label.place(x=225, y=y_positions[i], height=35, width=200)
    results.append(result_label)


weather_climate_result, weather_description_result, temp_result, pre_result = results

root.mainloop()
