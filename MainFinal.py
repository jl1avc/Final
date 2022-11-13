# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 03:18:08 2022

@author: Jon
"""

from Shelf import Shelf

import csv
from os import chdir

userInput1 = userInput2 = userInput3 = userInput4 = userInput5 = ''

shelfObj = Shelf()

try:
    chdir('D:/')
    
    with open('paper.csv', 'r') as csv_file:
        loadCSV = csv.reader(csv_file)
        
        next(loadCSV)
        for line in loadCSV:
            Shelf.LoadBook(shelfObj, line[0], line[1], line[2], line[3], line[4])
except FileNotFoundError:
    print('file not found')
    

Shelf.LoadBook(shelfObj, 'Harry Potter and the Sorcerer\'s Stone',
               'J. K. Rowling', 200,'Fiction','Harry Potter')
Shelf.LoadBook(shelfObj, 'Harry Potter and the Chamber of Secrets',
                      'J. K. Rowling', 300, 'Fiction','Harry Potter')
Shelf.LoadBook(shelfObj, 'Harry Potter and the Prisoner of Azkaban',
                      'J. K. Rowling', 400, 'Fiction','Harry Potter')
Shelf.LoadBook(shelfObj, 'Introduction to Computation and Programming Using Python',
                      'John V. Guttag', 637, 'Text','Programming')
Shelf.LoadBook(shelfObj, 'Discrete Mathematics: An Open Introduction',
                      'Oscar Levin', 394, 'Text','Math')
Shelf.LoadBook(shelfObj, 'Silent Spring',
                      'Rachel Carson', 300, 'Non-fiction','')
Shelf.LoadBook(shelfObj, 'The Fellowship of the Ring',
                      'J. R. R. Tolkien', 400, 'Fiction','The Lord of the Rings')
Shelf.LoadBook(shelfObj, 'Two Towers',
                      'J. R. R. Tolkien', 450, 'Fiction','The Lord of the Rings')

while userInput1 != '6':
    userInput1 = ''
    count = 0
    print('*********************************')
    print('\n1.Add Book\n2.Show all Books\n3.Remove a Book\n4.Find Books\n5.List Genres\n6.Exit')
    userInput1 = input('Enter a number(1-6): ')
    print('*********************************')
    
    if userInput1 == '1':
        Shelf.AddBook(shelfObj)
        
    elif userInput1 == '2':
        Shelf.ShowBooks(shelfObj)   
        
    elif userInput1 == '3':
        Shelf.Remove(shelfObj)
        
    elif userInput1 == '4':
        Shelf.FindBooks(shelfObj)
        
    elif userInput1 == '5':
        Shelf.ListGenres(shelfObj)
        
    else:
            pass