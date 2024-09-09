from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Weight Converter")
window.geometry("600x300")  
window.configure(bg='white')

#Calculation for Amount Enter to convert to desired results.
def sum1():
    try:
        weight = float(weight1.get())
        if v1.get() == 1:  # LBS to KG is checked
            ans = weight * 0.45
            result.delete(0, END)  # Clear the result Entry box before showing the result
            result.insert(0, f"{ans:.2f} kg")  # Insert the result in KG format
        elif v2.get() == 1:  # KG to LBS is checked
            ans = weight / 0.45
            result.delete(0, END)
            result.insert(0, f"{ans:.2f} lbs")  # Insert the result in LBS format
        else:
            messagebox.showwarning("Selection Error", "Please select a conversion option.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
        

p1 = PhotoImage(file='weight.png')
window.iconphoto(True, p1)

# Labels and entries
label1 = Label(window, text="Enter Amount:", font=('Arial', 25), fg='black', bg='white')
label1.grid(row=0, column=0, padx=10, pady=10)
label2 = Label(window, text="Weight:", font=('Arial', 25), fg='black', bg='white')
label2.grid(row=1, column=0, padx=10, pady=10)

weight1 = Entry(window)
weight1.grid(row=0, column=1, padx=10, pady=10)
result = Entry(window)
result.grid(row=1, column=1, padx=10, pady=10)



# Button placed in the next row
button = Button(window, text="Calculate", font=('Arial', 25), fg='black', command=sum1)
button.grid(row=4, column=1, columnspan=2, pady=20)

v1 = IntVar()
v2 = IntVar()

check_button1 = Checkbutton(window,text="LBS to KG",variable=v1)
check_button1.grid(row=0, column=4, columnspan=2, pady=10)  

check_button2 = Checkbutton(window,text="KG to LBS",variable=v2)
check_button2.grid(row=1, column=4, columnspan=2, pady=10) 

window.mainloop()
