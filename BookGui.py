# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:47:53 2022

@author: Jon
"""


from Shelf import Shelf
from tkinter import *
from tkinter import messagebox
import csv
import os
from os import chdir


def genres():
    msgTxt = Shelf.guiListGenres(shelfObj)
    messagebox.showinfo(message=msgTxt)

def add():
    Shelf.LoadBook(shelfObj, entryBox.get(), entryBox2.get(), \
                   entryBox3.get(), entryBox4.get(), entryBox5.get())
    global maxBooks
    listbox.insert(END, shelfObj.guiGet(maxBooks))
    maxBooks += 1

def delete():
    if listbox.curselection() != ():
        global maxBooks
        index = listbox.curselection()
        listbox.delete(index)
        Shelf.guiRemove(shelfObj, index[0])
        maxBooks -= 1

def show():
    Shelf.ShowBooks(shelfObj) 
    
def sample():
    global maxBooks

    try:
        chdir('D:/')
        
        with open('paper.csv', 'r') as csv_file:
            loadCSV = csv.reader(csv_file)
            next(loadCSV)
            for line in loadCSV:
                Shelf.LoadBook(shelfObj, line[0], line[1], line[2], line[3], line[4])
                listbox.insert(maxBooks, shelfObj.guiGet(maxBooks))
                maxBooks += 1
    except FileNotFoundError:
        print('file not found')

    Shelf.LoadBook(shelfObj, 'Harry Potter and the Sorcerer\'s Stone',
                   'J. K. Rowling', '200','Fiction','Harry Potter')
    Shelf.LoadBook(shelfObj, 'Harry Potter and the Chamber of Secrets',
                          'J. K. Rowling', '300', 'Fiction','Harry Potter')
    Shelf.LoadBook(shelfObj, 'Harry Potter and the Prisoner of Azkaban',
                          'J. K. Rowling', '400', 'Fiction','Harry Potter')
    Shelf.LoadBook(shelfObj, 'Introduction to Computation and Programming Using Python',
                          'John V. Guttag', '637', 'Text','Programming')
    Shelf.LoadBook(shelfObj, 'Discrete Mathematics: An Open Introduction',
                          'Oscar Levin', '394', 'Text','Math')
    Shelf.LoadBook(shelfObj, 'Silent Spring',
                          'Rachel Carson', '300', 'Non-fiction','')
    Shelf.LoadBook(shelfObj, 'The Fellowship of the Ring',
                          'J. R. R. Tolkien', '400', 'Fiction','The Lord of the Rings')
    Shelf.LoadBook(shelfObj, 'Two Towers',
                          'J. R. R. Tolkien', '450', 'Fiction','The Lord of the Rings')

    for i in range(8):
        listbox.insert(maxBooks,shelfObj.guiGet(maxBooks))
        maxBooks += 1
    

window = Tk()

window.title("Catalog program")
#file = None

window_width = 1280
window_height = 720
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

frame = Frame(window)
frame1 = Frame(window)
frame2 = Frame(window)
frame.pack()
frame1.pack()
frame2.pack()

scroll_bar = Scrollbar(frame1, orient=VERTICAL)
scroll_barH = Scrollbar(frame1, orient=HORIZONTAL)

scroll_bar.pack(side=RIGHT, fill=Y)
scroll_barH.pack(side=BOTTOM, fill=X)

shelfObj = Shelf()

Button(frame,text="   TITLE   ",font=("Consolas",25),width=12).pack(side=LEFT)
Button(frame,text="   AUTHOR   ",font=("Consolas",25),width=12).pack(side=LEFT)
Button(frame,text="   LENTGH   ",font=("Consolas",25),width=12).pack(side=LEFT)
Button(frame,text="   GENRE   ",font=("Consolas",25),width=12).pack(side=LEFT)
Button(frame,text="   SERIES   ",font=("Consolas",25),width=12).pack(side=LEFT)

listbox = Listbox(frame1,
                  bg="#f7ffde",
                  font=("Arial",18),
                  width=85,
                  height=17,
                  selectmode=SINGLE,xscrollcommand=scroll_barH.set,
                  yscrollcommand=scroll_bar.set)
listbox.pack(side=BOTTOM)

scroll_barH.config(command=listbox.xview)
scroll_bar.config(command=listbox.yview)

maxBooks = 0

Label(frame2,text="Title: ",font=14).grid(row=0,column=0)
Label(frame2,text="Author: ",font=14).grid(row=1,column=0)
Label(frame2,text="Length: ",font=14).grid(row=2,column=0)
Label(frame2,text="Genre: ",font=14).grid(row=3,column=0)
Label(frame2,text="series: ",font=14).grid(row=4,column=0)
entryBox = Entry(frame2)
entryBox.grid(row=0,column=1)
entryBox2 = Entry(frame2)
entryBox2.grid(row=1,column=1)
entryBox3 = Entry(frame2)
entryBox3.grid(row=2,column=1)
entryBox4 = Entry(frame2)
entryBox4.grid(row=3,column=1)
entryBox5 = Entry(frame2)
entryBox5.grid(row=4,column=1)

addButton = Button(frame2,text="add",command=add)
addButton.grid(row=5,column=1)

submitButton = Button(frame2,text="genres",command=genres)
submitButton.grid(row=5,column=2)

deleteButton = Button(frame2,text="delete",command=delete)
deleteButton.grid(row=5,column=3)

showButton = Button(frame2,text="CLprint",command=show)
showButton.grid(row=5,column=4)

sampleButton = Button(frame2,text="sample",command=sample)
sampleButton.grid(row=5,column=6)


    
    


window.mainloop()




