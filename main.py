from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=fb4892b88284661c55d867262bbb60eb"
    data = requests.get(url).json()

    if data.get("cod") != 200:  # error handling
        w_label1.config(text="N/A")
        wd_label1.config(text="City not found")
        temp_label1.config(text="N/A")
        per_label1.config(text="N/A")
    else:
        w_label1.config(text=data["weather"][0]["main"])
        wd_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=str(round(data["main"]["temp"] - 273.15, 2)) + " °C")
        per_label1.config(text=str(data["main"]["pressure"]) + " hPa")


win = Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x570")

# Label of Application
name_label = Label(win, text="Weather Application", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

# Input Field (Cities instead of states)
list_name = ["Delhi","Mumbai","Chennai","Kolkata","Bengaluru","Hyderabad","Pune","Jaipur","Lucknow","Ahmedabad"]
city_name = StringVar()
com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 15, "bold"), textvariable=city_name)
com.place(x=30, y=120, height=50, width=450)

# Labels
w_label = Label(win, text="Weather Climate", font=("Times New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Times New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

wd_label = Label(win, text="Weather Description", font=("Times New Roman", 17))
wd_label.place(x=25, y=330, height=50, width=210)
wd_label1 = Label(win, text="", font=("Times New Roman", 17))
wd_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text="", font=("Times New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Times New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)
per_label1 = Label(win, text="", font=("Times New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

# Button
done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()

