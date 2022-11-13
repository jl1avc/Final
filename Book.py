# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:18:44 2022

@author: Jon
"""


class Book(object):

    
    def __init__(self, title, aurthor, lentgh, genre, series):
        self.title = title
        self.author = aurthor
        self.lentgh = lentgh
        self.genre = genre
        self.series = series
        
        
    def prt(self):
        print('Title: ', self.title)
        print('Author: ', self.author)
        print('Lentgh: ', self.lentgh)
        print('Genre: ', self.genre)
        print('Series: ', self.series)
        print('---------------------------------')