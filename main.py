import tkinter as tk
from tkinter.ttk import *
from time import strftime
import datetime
#big font 
#font=("Arial Bold", 70)

#DECLARING ALL VARIABLES
global clockapp
global frame


#CREATING THE INSTANCE
clockapp = tk.Tk()
clockapp.title('CLOCK')
frame = tk.Frame(clockapp)


#MAKING THE TIME SHOWING AREA
string = tk.StringVar()
string = strftime('%H:%M:%S %p')
tk.Label(clockapp, text='[:--Time--:]', font=('San Sarif', 25), fg='Black').grid(row=0)
tk.Label(clockapp, text=string, font=("Arial", 20), fg='Red').grid(row=1)
tk.Label(clockapp, text='-------', font = ('Arial Bold',25)).grid(row=2)

#code for button
def alarm():
  import tkinter as tk
  Tab = tk.Toplevel()
  exec(open("files/alarm.py").read())

def stopwatch():
  import tkinter as tk
  Tab = tk.Toplevel()
  exec(open("files/stopwatch.py").read())

def timer():
  import tkinter as tk
  exec(open("files/timer.py").read())


#MAKING THE EXTRASSS
tk.Label(clockapp, text = 'Extras', font=('Arial Bold', 25), fg = 'Black').grid(row = 3)


#MAKING THE ALARM
photo = tk.PhotoImage(file = 'img/alarm.png')
photo = photo.subsample(3, 3)
tk.Button(clockapp,text=' Alarm ', image = photo, command =lambda:alarm(), compound='left').grid(row=4)

#MAKING THE STOPWATCH
photoTwo = tk.PhotoImage(file='img/stopwatch.png')
photoTwo = photoTwo.subsample(15, 15)
tk.Button(clockapp,text=' Stopwatch ', image = photoTwo, command =lambda:stopwatch(), compound='left').grid(row=5)

#MAKING THE TIMER 
photoThree = tk.PhotoImage(file='img/timer.png')
photoThree = photoThree.subsample(4, 4)
tk.Button(clockapp,text='       Timer ', image = photoThree,command=lambda:timer(), compound='left').grid(row=6)

clockapp.mainloop()