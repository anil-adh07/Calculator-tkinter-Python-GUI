from tkinter import *

window = Tk()
window.geometry("350x490")
window.title("MY CALCULATOR")
windowlabel = Label(window, text="CALCULATOR",bg='grey',font=("Times",20,'bold'))
windowlabel.pack()
window.config(background='grey')

textin = StringVar()
operator = ''

def clickbutton(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)

def equalbutton():
    global operator
    oprn = str(eval(operator))
    textin.set(oprn)
    operator = ''
    
def clearbutton():
    global operator
    textin.set('')
    operator = ''
 
windowtext = Entry(window,font=("courier New",14,'bold'),textvar = textin,width = 27,bd = 2, bg = 'white')
windowtext.pack(ipady=6)

but1 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(1),text="1",font=("Courier New", 14, 'bold'))
but1.place(x=25,y=90)

but2 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(2),text="2",font=("Courier New", 14, 'bold'))
but2.place(x=105,y=90)

but3 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(3),text="3",font=("Courier New", 14, 'bold'))
but3.place(x=185,y=90)

but4 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(4),text="4",font=("Courier New", 14, 'bold'))
but4.place(x=25,y=170)

but5 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(5),text="5",font=("Courier New", 14, 'bold'))
but5.place(x=105,y=170)

but6 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(6),text="6",font=("Courier New", 14, 'bold'))
but6.place(x=185,y=170)

but7 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(7),text="7",font=("Courier New", 14, 'bold'))
but7.place(x=25,y=250)

but8 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(8),text="8",font=("Courier New", 14, 'bold'))
but8.place(x=105,y=250)

but9 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(9),text="9",font=("Courier New", 14, 'bold'))
but9.place(x=185,y=250)

but0 = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton(0),text="0",font=("Courier New", 14, 'bold'))
but0.place(x=25,y=330)

butdot = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton("."),text=".",font=("Courier New", 14, 'bold'))
butdot.place(x=105,y=330)

butclr = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clearbutton(),text="CLR",font=("Courier New", 14, 'bold'))
butclr.place(x=265,y=90)

butadd = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton("+"),text="+",font=("Courier New", 14, 'bold'))
butadd.place(x=265,y=170)

butsub = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton("-"),text="-",font=("Courier New", 14, 'bold'))
butsub.place(x=265,y=250)

butmul = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton("*"),text="x",font=("Courier New", 14, 'bold'))
butmul.place(x=185,y=330)

butdiv = Button(window,padx=8, pady=8, bd=3, bg='white',command= lambda:clickbutton("/"),text="/",font=("Courier New", 14, 'bold'))
butdiv.place(x=265,y=330)


butequal = Button(window,padx=135, pady=8, bd=3,bg='white',command= lambda:equalbutton(),text="=",font=("Courier New", 14, 'bold'))
butequal.place(x=25,y=410)


window.mainloop()


