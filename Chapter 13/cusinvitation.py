#!python3
#this program reads guests.txt and creates a custom invitation for each guest
#you have to create invitations.docx with the style u want and name it 'Apples'

import os, docx

guestfile = open('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 13\\guests.txt')
guests = guestfile.read()
guestslist = guests.split('\n')
doc = docx.Document('invitations.docx')

for guest in guestslist:
    para1 = doc.add_paragraph('It would be the pleasure to have the company of')
    para1.style = 'Apples'
    para2 = doc.add_paragraph(guest)
    para2.style = 'Quote'
    para2.runs[0].bold = True
    para3 = doc.add_paragraph('at 11010 Memory Lane on the Evening of')
    para3.style = 'Apples'
    para4 = doc.add_paragraph('April 1st')
    para4.style = 'Quote'
    para5 = doc.add_paragraph('at 7 o\'clock')
    para5.style = 'Apples'
    doc.add_page_break()
doc.save('Custominvitations.docx')
print('done')
