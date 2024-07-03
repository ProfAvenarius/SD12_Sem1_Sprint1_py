#Description: A program featuring the tkinter library that opens a window with buttons that
#             emulates an GUI interface for the py programs. Exit ends the entire program.
#Author: Group 22 (DCE, NP)
#Date: Jun 18 - 26

#Program libraries


import tkinter as tk
from tkinter import *
import FizzBuzz                              #Importing other programs to respond to button
import Chocolate_Travel_Claims               #commands from GUI.
import Cool_Stuff_with_Strings_and_Dates
import XYZ_Company

#Program functions:


def FB():
    #activates FizzBuzz program in terminal
    FizzBuzz.main()
  
def MM():
   #Returns a message re: Main Menu
   print("***************************")
   print ("Main Menu ia already open.")
   print("***************************")

def SOSN():
   #Returns a message re: this program
   print("***************************")
   print ("Something Old Something New Is Currently Running.")
   print("***************************")

def CCT():
   #activates Chocolate_Travel_Claims program in terminal
   Chocolate_Travel_Claims.main()

def CSSD():
   #activates Cool_Stuff_with_Strings_and_Dates program in terminal
   Cool_Stuff_with_Strings_and_Dates.main()

def XYZC():
   #activates the XYZ Company program
   XYZ_Company.main()


def main():
  #Create the root window and immediately withdraw it
  root = tk.Tk()
  root.withdraw()
  top = tk.Toplevel()
  top.title('Press button to activate program.')
  top.geometry('920x530+200+120')
  top.configure(background="#BDE4FC")
  top.resizable(False, False)



  opt_one_label = tk.Label(
    top,
    text= "Press for Program 1 Employee Travel Claim", 
    font=('krungthep',16),
    wraplength=250,
    background="#BDE4FC"
  )


  opt_one = tk.Button(
    top,
    width=2,
    height=2,
    text= "●",
    command= CCT,
    font=('Ariel 18 bold'),
    foreground = "red",
    highlightbackground= "#5B5453",
    highlightthickness= 25,
    highlightcolor= "red",
    activebackground= "black",
    activeforeground= "dark red",
    cursor= 'hand1')


  opt_two_label = tk.Label(
    top,
    text= "Press for Program 2 The FizzBiss Problem",
    font=('krungthep', 16),
    wraplength=240,
    background="#BDE4FC"
  )

  opt_two = tk.Button(
    top,
    width=2,
    height=2,
    text= "●",
    command=FB,
    font=('Ariel 18 bold'),
    foreground = "red",
    highlightbackground= "#5B5453",
    highlightthickness= 25,
    highlightcolor= "red",
    activebackground= "black",
    activeforeground= "dark red",
    cursor= 'hand1')

  opt_three_label = tk.Label(
    top,
    text= "Press for Program 3 Cool Stuff with Strings and Dates",
    font=('krungthep',16),
    wraplength=240,
    background="#BDE4FC"
  )

  opt_three = tk.Button(
    top,
    width=2,
    height=2,
    text= "●",
    command=CSSD,
    font=('Ariel 18 bold'),
    foreground = "red",
    highlightbackground= "#5B5453",
    highlightthickness= 25,
    highlightcolor= "red",
    activebackground= "black",
    activeforeground= "dark red",
    cursor= 'hand1')


  opt_four_label = tk.Label(
    top,
    text= "Press for Program 4 XYZ Company Maintenance Schedule",
    font=('krungthep',16),
    wraplength=240,
    background="#BDE4FC"
  )

  opt_four = tk.Button(
    top,
    width=2,
    height=2,
    text= "●",
    command =XYZC,
    font=('Ariel 18 bold'),
    foreground = "red",
    highlightbackground= "#5B5453",
    highlightthickness= 25,
    highlightcolor= "red",
    activebackground= "black",
    activeforeground= "dark red",
    cursor= 'hand1')

  opt_five_label = tk.Label(
    top,
    text= "Press for Program 5 Something Old, Something New",
    font=('krungthep',16),
    wraplength=240,
    background="#BDE4FC"
  )

  opt_five = tk.Button(
    top,
    width=2,
    height=2,
    text= "●",
    command = SOSN,
    font=('Ariel 18 bold'),
    foreground = "red",
    highlightbackground= "#5B5453",
    highlightthickness= 25,
    highlightcolor= "red",
    activebackground= "black",
    activeforeground= "dark red",
    cursor= 'hand1')

  opt_six_label = tk.Label(
    top,
    text= "Press for Program 6 Main Menu",
    font=('krungthep',16),
    wraplength=240,
    background="#BDE4FC"
  )

  opt_six = tk.Button(
    top,
    width=2,
    height=2,
    text= "●",
    command=MM,
    font=('Ariel 18 bold'),
    foreground = "red",
    highlightbackground= "#5B5453",
    highlightthickness= 25,
    highlightcolor= "red",
    activebackground= "black",
    activeforeground= "dark red",
    cursor= 'hand1')

  opt_seven_label = tk.Label(
    top,
    text= "EXIT",
    font=('krungthep'),
    background="#BDE4FC"
  )

  opt_seven = tk.Button(
    top,
    width=3,
    height=1,
    text= "●",
    command = top.destroy,
    font=('Ariel 18 bold'),
    foreground = "red",
    highlightbackground= "#5B5453",
    highlightthickness= 10,
    highlightcolor= "red",
    activebackground= "black",
    activeforeground= "dark red",
    cursor= 'hand1')






  opt_one_label.grid(row = 1, column =1, padx=(50,10), pady=(5,5))
  opt_one.grid(row = 1, column =2, padx=(20,40), pady=(30,15))
  opt_two_label.grid(row = 1, column =3)
  opt_two.grid(row = 1, column =4, padx=(40,40), pady=(30,15))
  opt_three_label.grid(row = 2, column =1, padx=(50,10))
  opt_three.grid(row = 2, column =2, padx=(20,40),pady=(15,15))
  opt_four_label.grid(row = 2, column =3)
  opt_four.grid(row = 2, column =4, padx=(40,40), pady=(15,15))
  opt_five_label.grid(row = 3, column =1, padx=(50,10))
  opt_five.grid(row = 3, column =2, padx=(20,40),pady=(15,20))
  opt_six_label.grid(row = 3, column =3)
  opt_six.grid(row = 3, column =4, padx=(40,40), pady=(15,20))
  opt_seven_label.grid(row = 4, column =3, padx= (200,0))
  opt_seven.grid(row = 4, column = 4, padx=(40,40), pady=(15,20))
  #output_line.pack()

  top.mainloop()
  

if __name__ == "__main__":
    main()