from tkinter import *
import time
from PIL import ImageTk, Image

root = Tk()
bg=PhotoImage(file="weather_images/weather_350x350.png")
my_label = Label(root, image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

def getWeather():
    import requests, json

    city_name = textField.get()

    api = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=69bf0a590576448ed0bfd804ac2b2694"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    tempc = int(json_data['main']['temp'] - 273.15) #celsius
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    icon=json_data['weather'][0]['icon']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    tempf = (9*tempc)/5+32 #farenheit

    final_info = condition + "\n" + str(tempc) + "°C" + "\n" + str(tempf) + "°F"
    final_data = "\n"+ "Pressure : " + str(pressure) + " mb" + "\n" +"Humidity : " + str(humidity) + "\n" +"Wind Speed : " + str(wind) + "\n" + "Sunrise : " + sunrise + "\n" + "Sunset : " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

    photo = PhotoImage(file=f"weather_images/{icon}.png")
    photo_label.config(image=photo)
    photo_label.image = photo

#root.wm_attributes('-transparentcolor', 'red') - For making transparent.

textField = Entry(root)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)


b = Button(root, text="Get weather data", command=getWeather, bg="#ffffff")
b.pack(pady=10)

label1=Label(root, bg="#ffffff")
label1.pack()

label2=Label(root, bg="#ffffff")
label2.pack()

photo_label=Label(root, bg="#14d2fe")
photo_label.pack()


root.title("PyWeather")
root.iconbitmap("weather_images/weather.ico")
root.attributes('-alpha',0.9)
root.geometry("350x350")


root.mainloop()
