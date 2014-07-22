#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

How to determine the length of a bytes object in Python?

¿Cómo determinar la longitud de un objeto bytes de Python?
'''

#create a string
s = 'canción, 傰'
print(s)

#know the length of the string using the len() function
print(len(s))

#create a bytes object
b = bytes(s, 'utf8')
print(b)

#know the length of the bytes object using the len() function
print(len(b))
