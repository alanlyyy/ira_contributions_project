"""
	Creates a graphical user interface to use the ira contributions class.

	Changes made: Embedded matplotlib graph onto tkinter graphical user interface

	Author: Alan Ly 11-10-18
"""

import tkinter as tk
from ira_calculations_class import Portfolio_year

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

from PIL import ImageTk, Image


class Page(tk.Frame):
	"""
		Parent class to make different pages
		Also a subclass of the tkinter frame object
	"""

	def __init__(self, *args, **kwargs):
		#initialize tk.Frame to not overwrite the init method of tk.Frame
		tk.Frame.__init__(self,*args,**kwargs)

		self.Font = ("Helvetica",10)

	def show(self):
		#changes tkinter Frames whenever invoked
		self.lift()

class AboutPage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		text = "(C) Alan Ly \n 11-10-18 \n Test application v1"
		Label = tk.Label(self, text=text, font=self.Font)
		Label.pack(side="top", fill="both", expand=True)

class WelcomePage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)

		text = "Welcome to my IRASimulator"

		Label = tk.Label(self, text=text, font=self.Font)
		Label.pack(side="top", fill="both", expand=True)

		#add image to welcome page
		img = ImageTk.PhotoImage(Image.open("ira.png"))
		panel = tk.Label(self, image = img)
		panel.pack(side = "bottom", fill = "both", expand = "yes")

		#redeclare the image label because python sends the above image to
		#garbage collectionm
		panel.configure(image=img)
		panel.image = img

class FrontendPage(Page):

	def __init__(self, *args, **kwargs):

		Page.__init__(self, *args, **kwargs)

		self.myPortfolio = Portfolio_year(0)

		#create tk.Labels for that object
		self.t1 = tk.Label(self, text="Contribution", font=self.Font)
		self.t1.grid(row=1,column=0)

		self.t2 = tk.Label(self, text="Interest",font=self.Font)
		self.t2.grid(row=2,column=0)

		self.t3 = tk.Label(self, text="Years",font=self.Font)
		self.t3.grid(row=3,column=0)

		self.t5 = tk.Label(self, text= "Balance",font=self.Font)
		self.t5.grid(row=1, column=2)

		self.t6 = tk.Label(self, text= "No. Years",font=self.Font)
		self.t6.grid(row=2, column=2)

		self.t7= tk.Label(self, text="Prev Balance",font=self.Font)
		self.t7.grid(row=3, column=2)

		self.t8 = tk.Label(self, text="Prev. No. Year",font=self.Font)
		self.t8.grid(row=4, column=2)

		#===========================================================================================
		#stores the values of the current balance, current year, prev balance, prev year
		self.current_balance = tk.StringVar()
		self.current_balance_hold = tk.Label(self, textvariable=self.current_balance, font=self.Font)
		self.current_balance_hold.grid(row=1,column=3)

		self.current_year = tk.IntVar()
		self.current_years_hold = tk.Label(self, textvariable=self.current_year,font=self.Font)
		self.current_years_hold.grid(row=2,column=3)

		self.prev_balance = tk.StringVar()
		self.prev_balance_hold = tk.Label(self, textvariable=self.prev_balance,font=self.Font)
		self.prev_balance_hold.grid(row=3,column=3)

		self.prev_year = tk.IntVar()
		self.prev_year_hold = tk.Label(self, textvariable=self.prev_year,font=self.Font)
		self.prev_year_hold.grid(row=4,column=3)
		#====================================================================

		#====================================================================
		#user entry windows
		self.t1_entry = tk.StringVar()
		self.t2_entry = tk.StringVar()
		self.t3_entry = tk.StringVar()
		self.t4_entry = tk.StringVar()

		self.e1 = tk.Entry(self, textvariable=self.t1_entry)
		self.e1.grid(row=1,column=1)
		self.e2 = tk.Entry(self, textvariable=self.t2_entry)
		self.e2.grid(row=2,column=1)
		self.e3 = tk.Entry(self, textvariable=self.t3_entry)
		self.e3.grid(row=3,column=1)
		self.e4 = tk.Entry(self, textvariable=self.t4_entry)
		self.e4.grid(row=5,column=1)
		#=====================================================================
		self.clear_button = tk.Button(self,text="Clear", height=1,width=10,font=self.Font,command=self.clear_button_action)
		self.clear_button.grid(row=8,column=0)

		self.submit_button = tk.Button(self,text="Submit", height=1,width=10,font=self.Font,command=self.submit_button_action)
		self.submit_button.grid(row=8,column=1)

		self.withdraw_button = tk.Button(self,text="Withdraw", height=1, width=10, font=self.Font, command=self.withdraw_button_action)
		self.withdraw_button.grid(row=5, column=0)

		self.quit_button = tk.Button(self,text='Quit', font=self.Font, command=self.quit_button_action)
		self.quit_button.grid(row=31,column=0)

		#Draw/plot figure in tkinter embedded window
		self.plot_data(self.myPortfolio.list_dollars)
		
		#self.mainloop()

	def plot_data(self,dollars):
		"""
			This function takes in a list for dollars calculates
			the years and converts the lists into numpy arrays and plots 
			them onto a matplotlib figure embedded into tkinter.

		"""
		#create a figure object to hold the matplotlib plots
		self.figure = Figure(figsize=(5,4), dpi = 100)

		#create a subplot first row first column
		self.a = self.figure.add_subplot(111)

		#update the list of dollars for the plot
		self.dollars = np.array(dollars)
		self.years = np.arange(0,len(dollars),1)

		#plots the numpy arrays into a matplotlib figure 'pyplot'
		self.a.plot(self.years,self.dollars,linestyle='none',marker='o')

		#holds matplotlib figure in a container to be displayed in tkinter window 'window'
		self.canvas = FigureCanvasTkAgg(self.figure,master=self)

		#show matplotlib figure on tkinter window
		self.canvas.show()

		#displays the matplotlib figure on the grid
		self.canvas.get_tk_widget().grid(row=10,column=1,columnspan=3,rowspan=20)

		#create the toolbar synced with canvas
		self.toolbarFrame = tk.Frame(self)
		self.toolbarFrame.grid(row=31,column=1)

		#creates a navigation toolbar linked to the matplotlib figure with
		#the master being the toolbar tk.Frame
		self.toolbar = NavigationToolbar2TkAgg(self.canvas,self.toolbarFrame)

		#update the plot
		self.toolbar.update()


	def quit_button_action(self):
		self.quit()
		self.destroy()

	def submit_button_action(self):

		if len(self.t1_entry.get()) == 0 or \
				len(self.t2_entry.get()) == 0 or len(self.t3_entry.get()) == 0  \
								or float(self.t1_entry.get()) > 5500:
			pass

		else:
			contribution = float(self.t1_entry.get())
			intrest = float(self.t2_entry.get())
			num_years = int(self.t3_entry.get())

			self.myPortfolio.balance(contribution,intrest,num_years)

		#pull values from the myPortfolio class and displays them onto the graphical user interface
		self.current_balance.set(round(self.myPortfolio.current_balance,2))
		self.prev_balance.set(round(self.myPortfolio.prev_balance,2))
		self.current_year.set(int(self.myPortfolio.num_year_contributions))
		self.prev_year.set(int(self.myPortfolio.prev_num_year_contributions))

		#pulls the updated list of dollars from myPortfolio class and plots data
		#using matplotlib embedded into tkinter
		self.plot_data(self.myPortfolio.list_dollars)




	def clear_button_action(self): 
		self.myPortfolio.clear()  #clear all values in the Portfolio_year class

		#update new values after clearing the previous values
		self.current_balance.set(round(self.myPortfolio.current_balance,2))			
		self.prev_balance.set(round(self.myPortfolio.prev_balance,2))
		self.current_year.set(int(self.myPortfolio.num_year_contributions))
		self.prev_year.set(int(self.myPortfolio.prev_num_year_contributions))

		#plot the updated list of values
		self.plot_data(self.myPortfolio.list_dollars)

	def withdraw_button_action(self):
		if self.myPortfolio.num_year_contributions < 5:
			pass
		else:
			#updates values after withdrawing from the balance
			self.myPortfolio.withdraw(float(self.t4_entry.get()))
			self.current_balance.set(round(self.myPortfolio.current_balance,2))
			self.prev_balance.set(round(self.myPortfolio.prev_balance,2))
			self.current_year.set(int(self.myPortfolio.num_year_contributions))
			self.prev_year.set(int(self.myPortfolio.prev_num_year_contributions))

		#plot the updated list of values
		self.plot_data(self.myPortfolio.list_dollars)

class MainView(tk.Frame):

	def __init__(self, *args, **kwargs):

		#initialize the tk.Frame class to prevent overwriting the init method
		tk.Frame.__init__(self, *args, **kwargs)

		#initialize the Pages
		p3 = FrontendPage(self)
		p2 = AboutPage(self)
		p1 = WelcomePage(self)

		#holds the buttons in the base frame
		buttonFrame = tk.Frame(self)

		#holds the pages in the base frame
		container = tk.Frame(self)

		buttonFrame.pack(side="top", fill="x", expand=False)
		container.pack(side="top", fill="both", expand=True)

		p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

		b1 = tk.Button(buttonFrame, text="Welcome Page", command=p1.lift)
		b1.pack(side = "left")
		b2 = tk.Button(buttonFrame, text="About Page", command=p2.lift)
		b2.pack(side = "left")
		b3 = tk.Button(buttonFrame, text="Simulator Page", command=p3.lift)
		b3.pack(side = "left")

		p1.show()
#=========================================================================================== 
if __name__ == '__main__':
	window = tk.Tk()
	window.title("IRASimulator")
	main = MainView(window)
	main.pack(side="top", fill="both", expand=True)
	window.wm_geometry("600x600")
	window.mainloop()
