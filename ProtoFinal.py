# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:12:43 2022

@author: Jon
"""
'''-------------------------------------------------------------
from Book import Book

userInput1 = userInput2 = userInput3 = userInput4 = userInput5 = ''

def AddBook():
    userInput1 = input('Enter title: ')
    userInput2 = input('Enter author: ')
    userInput3 = input('Enter length: ')
    userInput4 = input('Enter genre: ')
    userInput5 = input('Enter series: ')

    bookList1.append(Book(userInput1, userInput2, userInput3, userInput4, userInput5))
    
def ShowBooks():
    for i in range(len(bookList1)):
        bookList1[i].prt()

def Remove():
    userInput1 = input('Enter title to remove: ')
    for i in range(len(bookList1)):
        if bookList1[i].title == userInput1:
            print('\nRemoving: ')
            bookList1[i].prt()
            bookList1.remove(bookList1[i])
            break

def FindBooks():
    count = 0
    print('\nSearch by\n1.Title\n2.Author\n3.Genre\n4.Series\n5.Back to main menu')
    userInput1 = input('Enter a number(1-5): ')
    
    if userInput1 == '1':
        userInput1 = input('Enter Book Title: ')
        for i in range(len(bookList1)):
            if bookList1[i].title == userInput1:
                print('\nBook Found: ')
                bookList1[i].prt()
                count += 1
                continue
        
    elif userInput1 == '2':
        userInput1 = input('Enter Book Author: ')
        for i in range(len(bookList1)):
            if bookList1[i].author == userInput1:
                print('\nBook Found: ')
                bookList1[i].prt()
                count += 1
                continue  
        
    elif userInput1 == '3':
        userInput1 = input('Enter Book Genre: ')
        for i in range(len(bookList1)):
            if bookList1[i].genre == userInput1:
                print('\nBook Found: ')
                bookList1[i].prt()
                count += 1
                continue
        
    elif userInput1 == '4':
        userInput1 = input('Enter Series Title: ')
        for i in range(len(bookList1)):
            if bookList1[i].series == userInput1:
                print('\nBook Found: ')
                bookList1[i].prt()
                count += 1
                continue
        
    else:
        pass
    print('found ', count, 'Books')
    
def ListGenres():
    genresList1  = {}
    genresCount1 = []
    
    for i in range(len(bookList1)):
        genresCount1.append(0)
        
    for i in range(len(bookList1)):
        for j in range(len(bookList1)):
            if bookList1[i].genre == bookList1[j].genre:
                genresCount1[i] += 1
                genresList1[bookList1[i].genre] = genresCount1[i]
    
    print('Genres:')            
    for key, value in genresList1.items():
        if key != '':
            print(key, ' : ', value)
        elif key == '':
            print('No genre : ', value)
        else:
            pass


#Main=========================================================
bookList1 = []
bookList1.append(Book('Harry Potter and the Sorcerer\'s Stone',
                      'J. K. Rowling', 200, 'Fiction','Harry Potter'))
bookList1.append(Book('Harry Potter and the Chamber of Secrets',
                      'J. K. Rowling', 300, 'Fiction','Harry Potter'))
bookList1.append(Book('Harry Potter and the Prisoner of Azkaban',
                      'J. K. Rowling', 400, 'Fiction','Harry Potter'))
bookList1.append(Book('Introduction to Computation and Programming Using Python',
                      'John V. Guttag', 637, 'Text','Programming'))
bookList1.append(Book('Discrete Mathematics: An Open Introduction',
                      'Oscar Levin', 394, 'Text','Math'))
bookList1.append(Book('Silent Spring',
                      'Rachel Carson', 300, 'Non-fiction',''))
bookList1.append(Book('The Fellowship of the Ring',
                      'J. R. R. Tolkien', 400, 'Fiction','The Lord of the Rings'))
bookList1.append(Book('Two Towers',
                      'J. R. R. Tolkien', 450, 'Fiction','The Lord of the Rings'))

while userInput1 != '6':
    userInput1 = userInput2 = userInput3 = userInput4 = userInput5 = ''
    count = 0
    print('*********************************')
    print('\n1.Add Book\n2.Show all Books\n3.Remove a Book\n4.Find Books\n5.List Genres\n6.Exit')
    userInput1 = input('Enter a number(1-6): ')
    print('*********************************')
    
    if userInput1 == '1':
        AddBook()
        
    elif userInput1 == '2':
        ShowBooks()   
        
    elif userInput1 == '3':
        Remove()
        
    elif userInput1 == '4':
        FindBooks()
        
    elif userInput1 == '5':
        ListGenres()
        
    else:
        pass
