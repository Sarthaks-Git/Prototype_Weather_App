import requests 
import customtkinter
import tkinter
import json
import win32com.client as wincom
from PIL import Image
speak=wincom.Dispatch("SAPI.SpVoice") #text to speech 
city="" 
temp=""

def check():
    global city,temp
    city=entry.get()
    url=f"http://api.weatherapi.com/v1/current.json?key=89b0a5a790814fc9a6c183515242204&q={city}"
    r=requests.get(url)
    weatherdict=json.loads(r.text)

    temp=weatherdict["current"]["temp_c"]
    condition=weatherdict["current"]["condition"]["text"]
    lb3=customtkinter.CTkLabel(frame,text=f"Temperature is {temp}°C\n{condition}",font=("Century Gothic",20))
    lb3.place(x=90,y=150)
    speak.Speak(f'The Current weather in {city} is {weatherdict["current"]["temp_c"]} degree Celcius')

mode="Light"
def switcher():
    global mode
    if mode=="Dark":
        customtkinter.set_appearance_mode("dark")
        mode="Light"
    else:
        customtkinter.set_appearance_mode("light")
        mode="Dark"
 
print(temp)
window=customtkinter.CTk()
my_image=customtkinter.CTkImage(light_image=Image.open('./Background/LTMD.jpg'),dark_image=Image.open('./Background/DKMD.jpg'),size=(1366,768))
lb1=customtkinter.CTkLabel(master=window,text="",image=my_image,anchor="center")
lb1.pack()
#FRAME
ttle=customtkinter.CTkLabel(window,text="Prototype Weather App",font=("Century Gothic",30),corner_radius=500,bg_color="transparent",fg_color="transparent")
ttle.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)
frame=customtkinter.CTkFrame(master=lb1,
                             width=400,
                             height=360,
                             corner_radius=15)
frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

entry=customtkinter.CTkEntry(frame,
                             placeholder_text="Enter the City",
                             width=200,
                             font=("Century Gothic",25))
check_button=customtkinter.CTkButton(frame,
                                      text="Check",
                                      font=('Century Gothic',25),
                                      height=38,
                                      command=check)
check_button.place(x=235,y=50)

entry.place(x=25,y=50)
window.geometry("550x700")
window.title("Weather App")

switch_var=customtkinter.StringVar(value="On")
my_switch=customtkinter.CTkSwitch(frame,
                                  text="Dark Mode",
                                  font=("Century Gothic",13),
                                  command=switcher,
                                  variable=switch_var,
                                  onvalue="On",
                                  offvalue="Off")
my_switch.place(x=280,y=330)
window.mainloop()

