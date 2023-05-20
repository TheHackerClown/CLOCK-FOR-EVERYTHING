# Python program to illustrate a stop watch
# using tk
#importing the required libraries
import tkinter as tk
from datetime import datetime
counter = 66600
running = False
def counter_label(label):
	def count():
		if running:
			global counter

			# To manage the initial delay.
			if counter==66600:			
				display="starting..."
			else:
				tt = datetime.fromtimestamp(counter)
				string = tt.strftime("%H:%M:%S")
				display=string

			label['text']=display # Or label.config(text=display)

			# label.after(arg1, arg2) delays by
			# first argument given in milliseconds
			# and then calls the function given as second argument.
			# Generally like here we need to call the
			# function in which it is present repeatedly.
			# Delays by 1000ms=1 seconds and call count again.
			label.after(1000, count)
			counter += 1

	# Triggering the start of the counter.
	count()	

# start function of the stopwatch
def start(label):
	global running
	running=True
	counter_label(label)
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

# stop function of the stopwatch
def stop():
	global running
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

# reset function of the stopwatch
def reset(label):
	global counter
	counter=66600

	# If rest is pressed after pressing stop.
	if running==False:	
		reset['state']='disabled'
		label['text']='Welcome!'

	# If reset is pressed while the stopwatch is running.
	else:			
		label['text']='starting...'

root = tk.Tk()
root.title("stopwatch")

# Fixing the window size.
root.minsize(width=250, height=70)
label = tk.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = tk.Frame(root)


tk.Button(f, text='Start', width=6, command=lambda: start(label)).pack(side="left")
tk.Button(f, text='Stop',width=6,state='disabled', command=lambda: stop()).pack(side="left")
tk.Button(f, text='Reset',width=6, state='disabled', command=lambda: reset(label)).pack(side="left")
f.pack(anchor = 'center',pady=5)
root.mainloop()
