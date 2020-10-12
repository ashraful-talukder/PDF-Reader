import pyttsx3
import PyPDF2

pdf = open('The_Da_Vinci_Code.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
pages = pdfReader.numPages

read = pyttsx3.init()
for i in range(0, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    read.say(text)
    read.runAndWait()