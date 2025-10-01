from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x425")
window.resizable(0,0)
window.configure(bg='white')
#p1 = PhotoImage(file='Calculator.png')
#window.iconphoto(True, p1)

def button_press(num):
    global expression
    expression = expression + str(num)
    expression_label.set(expression)
    

def button_clear():
    global expression
    expression = ""
    expression_label.set("")

def button_sum():
    global expression
    try:
        expression = expression.replace('x', '*')
        result = str(eval(expression))
        expression_label.set(result)
        expression = result
    except Exception as e:
        expression_label.set("Error")  
        expression = ""
        

expression = ""
expression_label = StringVar()
    

input_frame = Frame(window, width = 312, height = 80, bd = 0, highlightbackground = "grey", highlightcolor = "grey", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = expression_label, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

# Buttons frame
btns_frame = Frame(window, width = 350, height = 350, bg = "grey")
btns_frame.pack(fill=BOTH, expand=True)

# Row 1
clear = Button(btns_frame, text="AC", width=21, height=3, command=button_clear)
clear.grid(row=1, column=0, columnspan=3, padx=0, pady=1)

divide = Button(btns_frame, text="/", width=4, height=3, command=lambda: button_press("/"))
divide.grid(row=1, column=3, padx=0, pady=1)

# Row 2
seven = Button(btns_frame, text="7", width=4, height=3, command=lambda: button_press("7"))
seven.grid(row=2, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", width=4, height=3, command=lambda: button_press("8"))
eight.grid(row=2, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", width=4, height=3, command=lambda: button_press("9"))
nine.grid(row=2, column=2, padx=1, pady=1)

multiplication = Button(btns_frame, text="x", width=4, height=3, command=lambda: button_press("x"))
multiplication.grid(row=2, column=3, padx=1, pady=1)

# Row 3
four = Button(btns_frame, text="4", width=4, height=3, command=lambda: button_press("4"))
four.grid(row=3, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", width=4, height=3, command=lambda: button_press("5"))
five.grid(row=3, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", width=4, height=3, command=lambda: button_press("6"))
six.grid(row=3, column=2, padx=1, pady=1)

subtraction = Button(btns_frame, text="-", width=4, height=3, command=lambda: button_press("-"))
subtraction.grid(row=3, column=3, padx=1, pady=1)

# Row 4
one = Button(btns_frame, text="1", width=4, height=3, command=lambda: button_press("1"))
one.grid(row=4, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", width=4, height=3, command=lambda: button_press("2"))
two.grid(row=4, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", width=4, height=3, command=lambda: button_press("3"))
three.grid(row=4, column=2, padx=1, pady=1)

addition = Button(btns_frame, text="+", width=4, height=3, command=lambda: button_press("+"))
addition.grid(row=4, column=3, padx=1, pady=1)

# Row 5
zero = Button(btns_frame, text="0", width=12, height=3, command=lambda: button_press("0"))
zero.grid(row=6, column=0, columnspan=2, padx=1, pady=1)

decimal_point = Button(btns_frame, text=".", width=4, height=3, command=lambda: button_press("."))
decimal_point.grid(row=6, column=2, padx=1, pady=1)

equal = Button(btns_frame, text="=", width=4, height=3, command=button_sum)
equal.grid(row=6, column=3, padx=2, pady=1)

window.mainloop()
