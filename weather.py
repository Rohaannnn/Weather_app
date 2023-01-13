from configparser import ConfigParser
from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image

url= 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file='config.ini'
config=ConfigParser()
config.read(config_file)
api_key =config ['api key'] ['key']

def get_weather(city):
    result= requests.get(url.format(city ,api_key))
    if result:
        json=result.json()
        print(json)
        
        temp_kelvin=json['main'][ 'temp']
        result= {
          'city':json['name'],
          'country':json ['sys'] ['country'],
          'temp_celsius':temp_kelvin-273.15,
          'temp_fahrenheit':(temp_kelvin-273.15) * 9 / 5 +3,
          'icon': '{}@2x.png'.format(json ['weather'][0] ['icon']),
          'weather': json ['weather'] [0] ['main'],

        }
        
        # city= json['name']
        # country= json ['sys'] ['country']
        # temp_kelvin=json['main'][ 'temp']
        # temp_celsius=temp_kelvin-273.15
        # temp_fahrenheit=(temp_kelvin-273.15) * 9 / 5 +32
        # icon= json ['weather'][0] ['icon']
        # weather= json ['weather'] [0] ['main']
        # final= (city,country,temp_celsius,temp_fahrenheit,icon,weather)
        # return final
        return result 
    else:
        return None



def search():
    city=city_text.get()
    weather=get_weather(city)
    if weather:
      #location_lbl['text'] ='{},{}'.format(weather[0],weather[1])
      location_lbl['text'] ='{},{}'.format(weather['city'],weather['country'])

      # image['bitmap'] = 'weather_icons/{}.png'.format(weather[4])
      #image['image']=ImageTk.BitmapImage(Image.open('weather_icons/{}'.format(weather['icon'])))
      #image['bitmap'] = 'weather_icons/{}'.format(weather['icon'])
      # temp_lbl['text'] ='{:.2f}°C,{:.2f}°F'.format(weather[2], weather[3])
      temp_lbl['text'] ='{:.2f}°C,{:.2f}°F'.format(weather['temp_celsius'], weather['temp_fahrenheit'])
      weather_lbl['text']=weather['weather']
    else:
      messagebox.showerror('Error', 'cannot find city  {}'.format(city) )  


app=Tk()
app.title('Weather App')
app.geometry('750x350')

city_text=StringVar()
city_entry=Entry(app, textvariable=city_text)
city_entry.pack()

search_btn= Button(app, text='Search Weather' , width=12, command=search)
search_btn.pack()

location_lbl= Label(app, text='', font=('bold',20))
location_lbl.pack()

image=Label(app, bitmap='')
image.pack()

temp_lbl= Label(app, text='')
temp_lbl.pack()

weather_lbl=Label(app, text='')
weather_lbl.pack()




app.mainloop()