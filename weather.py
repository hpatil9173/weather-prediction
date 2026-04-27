import requests
import tkinter as tk

API_KEY = "5f6f8efb3705f97d8b68355833996b25"

def get_weather():
    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        result_label.config(
            text=f"City: {city}\nTemperature: {temp} °C\nWeather: {weather}"
        )
    else:
        result_label.config(text="City not found")

# Create window
# Window
window = tk.Tk()
window.title("Live Weather App")
window.geometry("800x550")
window.config(bg="#1e1e2f")

# Title
title = tk.Label(
    window,
    text="🌦 Live Weather App",
    font=("Helvetica", 35, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# City Entry
city_entry = tk.Entry(
    window,
    font=("Arial", 18),
    width=25,
    justify="center",
    bg="#f0f8ff",        # background color
    fg="#333333",        # text color
    bd=3,                # border thickness
    relief="groove",     # border style
    highlightthickness=2,
    highlightbackground="#4CAF50",
    highlightcolor="#4CAF50"
)

city_entry.pack(pady=15, ipady=6)

# Button
search_btn = tk.Button(
    window,
    text="Get Weather",
    font=("Arial", 18, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=15,
    pady=5,
    command=get_weather
)
search_btn.pack(pady=10)

# Result Box
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 20),
    bg="#2e2e3e",
    fg="white",
    width=31,
    height=5
)
result_label.pack(pady=20)

window.mainloop()