# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:18:20 2018

@author: 1449486
"""
import nltk
import PyPDF2
import pandas as pd
from PyPDF2 import PdfFileReader,PdfFileWriter

fileReader=PdfFileReader(open('new.pdf',"rb"))

fileReader.getNumPages()

page=fileReader.getPage(5)

print(page.cropBox.getLowerLeft())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())
print(page.cropBox.getLowerRight())

writer=PdfFileWriter()
text=""

for i in range (9,fileReader.getNumPages()):
    page=fileReader.getPage(i)
    page.cropBox.setLowerLeft((0, 50))
    page.cropBox.setUpperRight((612, 720))
    writer.addPage(page)
    
file1 = open('new1.pdf', 'wb')

writer.write(file1)

file1.close()



