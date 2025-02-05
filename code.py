from gtts import gTTS
import os
from tkinter import *



#for text to speach

#text = open('demo.txt','r').read()

#language='hi'
#output = gTTS(text=text, lang=language,slow=False)
#output.save('fileoutput.mp3')
#os.system("fileoutput.mp3")


root = Tk()
canvas = Canvas(root,width=400, height=300)
canvas.pack()

def texttospeach():
    text = entry.get()
    language='en'
    output = gTTS(text=text, lang=language,slow=False)
    output.save('output.mp3')
    os.system("output.mp3")

entry = Entry(root)
canvas.create_window(200,180,window=entry)

button = Button(text="start",command= texttospeach)
canvas.create_window(200,230,window=button)


root.mainloop()
