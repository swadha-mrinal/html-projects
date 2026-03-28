from tkinter import *

window = Tk()
window.title('tkinter sample window')
window.geometry('300x300')

greeting = Label(text = "Hello user",fg='black',bg='white')
Button = Button(text="click me",bg='black',fg='white')
entry = Entry(fg='yellow',bg='blue',width=50)
greeting.pack()
Button.pack()
entry.pack()

frame = Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
label = Label(master=frame,text='sample Frame')
label.pack()
textbox = Text(fg='green',bg='yellow')
textbox.pack()

window.mainloop()