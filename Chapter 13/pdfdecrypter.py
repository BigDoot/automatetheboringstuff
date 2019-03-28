#!python3
#this is a brute force pdf passwords breaker
#it reads dictionary.txt which contains 44,000 words and returns the single
#word that decrypts the pdf

import os, PyPDF2

file = open('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 13\\dictionary.txt')
stringofwords = file.read()
dictionary = stringofwords.split('\n')
pdffile = open('encryptedwatermark.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(pdffile)
passwordfound = False
for word in dictionary:
    if pdfreader.decrypt(word) == 1:
        print('Password is ' + word)
        passwordfound = True
        break
    if pdfreader.decrypt(word.lower()) == 1:
        print('Password is ' + word)
        passwordfound = True
        break
if passwordfound == False:
    print('Unable to decrypt Pdf file.')
