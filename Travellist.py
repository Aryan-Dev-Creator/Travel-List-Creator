# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:36:09 2022

@author: DarkSoulJoker
"""

from tkinter import*
import random

root=Tk()
root.title("Travel List Creator")
root.geometry("500x500")
root.configure(background="black")

enter_name = Entry(root)
enter_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)

travel_list = Label(root)

list1 = []

def addfriend():
    item_name = enter_name.get()
    list1.append(item_name)
    travel_list["text"] = "Your Travellist : " + str(list1)
    
    
btn = Button(root, text = "Add To The Travellist", command = addfriend, bg = "white", fg = "black")
btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)

travel_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)

    
root.mainloop()