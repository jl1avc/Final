# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 03:02:05 2022

@author: Jon
"""

from Book import Book

userInput1 = userInput2 = userInput3 = userInput4 = userInput5 = ''

class Shelf():
    
    def __init__(self):
        self.bookList1 = []
        
    def LoadBook(self, title, aurthor, lentgh, genre, series):
        self.bookList1.append(Book(title, aurthor, lentgh, genre, series))
        
    def AddBook(self):
        userInput1 = input('Enter title: ')
        userInput2 = input('Enter author: ')
        userInput3 = input('Enter length: ')
        userInput4 = input('Enter genre: ')
        userInput5 = input('Enter series: ')
    
        self.bookList1.append(Book(userInput1, userInput2, userInput3, userInput4, userInput5))
        
    def ShowBooks(self):
        for i in range(len(self.bookList1)):
            self.bookList1[i].prt()
    
    def Remove(self):
        userInput1 = input('Enter title to remove: ')
        for i in range(len(self.bookList1)):
            if self.bookList1[i].title == userInput1:
                print('\nRemoving: ')
                self.bookList1[i].prt()
                self.bookList1.remove(self.bookList1[i])
                break
    
    def FindBooks(self):
        count = 0
        print('\nSearch by\n1.Title\n2.Author\n3.Genre\n4.Series\n5.Back to main menu')
        userInput1 = input('Enter a number(1-5): ')
        
        if userInput1 == '1':
            userInput1 = input('Enter Book Title: ')
            for i in range(len(self.bookList1)):
                if self.bookList1[i].title == userInput1:
                    print('\nBook Found: ')
                    self.bookList1[i].prt()
                    count += 1
            
        elif userInput1 == '2':
            userInput1 = input('Enter Book Author: ')
            for i in range(len(self.bookList1)):
                if self.bookList1[i].author == userInput1:
                    print('\nBook Found: ')
                    self.bookList1[i].prt()
                    count += 1
            
        elif userInput1 == '3':
            userInput1 = input('Enter Book Genre: ')
            for i in range(len(self.bookList1)):
                if self.bookList1[i].genre == userInput1:
                    print('\nBook Found: ')
                    self.bookList1[i].prt()
                    count += 1
            
        elif userInput1 == '4':
            userInput1 = input('Enter Series Title: ')
            for i in range(len(self.bookList1)):
                if self.bookList1[i].series == userInput1:
                    print('\nBook Found: ')
                    self.bookList1[i].prt()
                    count += 1
            
        else:
            pass
        print('found ', count, 'Books')
        
    def ListGenres(self):
        genreDict  = {}
        genresCount1 = []
        
        for i in range(len(self.bookList1)):
            genresCount1.append(0)
            
        for i in range(len(self.bookList1)):
            for j in range(len(self.bookList1)):
                if self.bookList1[i].genre == self.bookList1[j].genre:
                    genresCount1[i] += 1
                    genreDict[self.bookList1[i].genre] = genresCount1[i]
        
        print('Genres:')            
        for key, value in genreDict.items():
            if key != '':
                print(key, ':', value)
            elif key == '':
                print('No genre :', value)
            else:
                pass
            
            
            
    def guiGet(self, i):
        bookString = self.bookList1[i].title + '  |  ' + self.bookList1[i].author + '  |  '+\
            self.bookList1[i].lentgh + '  |  '+ self.bookList1[i].genre + '  |  '+\
            self.bookList1[i].series
        return bookString
    
    def guiRemove(self, userInput1):        
        self.bookList1.remove(self.bookList1[userInput1])
        
    def guiListGenres(self):
        genreDict  = {}
        genresCount1 = []
        
        for i in range(len(self.bookList1)):
            genresCount1.append(0)
            
        for i in range(len(self.bookList1)):
            for j in range(len(self.bookList1)):
                if self.bookList1[i].genre == self.bookList1[j].genre:
                    genresCount1[i] += 1
                    genreDict[self.bookList1[i].genre] = genresCount1[i]
        txt = 'Genres: |'
        for key, value in genreDict.items():
            if key != '':
                #print(key, ':', value)
                
                txt = txt + key 
                txt = txt + ' : '
                txt = txt + str(value) + '  |  '
                
            elif key == '':
                #print('No genre :', value)
                txt = txt + 'No genre :' 
                txt = txt + str(value) + '  |  '
            else:
                pass
            
        return txt
            
            
            
            
            
            