import tkinter as tk  # Now I need a button which will display the output 
import numpy as np

root = tk.Tk()
root.geometry("650x400")
root.title("Calculator")

num1_var = tk.IntVar()
num2_var = tk.IntVar()

def update_output(result):

    t.delete("1.0", tk.END)
    t.insert("1.0", result)

def add():

    num1 = num1_var.get()
    num2 = num2_var.get()

    result = np.add(num1, num2)
    update_output(result)

def sub():

    num1 = num1_var.get()
    num2 = num2_var.get()

    result = np.subtract(num1, num2)
    update_output(result)

def mul():

    num1 = num1_var.get()
    num2 = num2_var.get()

    result = np.multiply(num1, num2)
    update_output(result)

def div():

    num1 = num1_var.get()
    num2 = num2_var.get()

    result = np.divide(num1, num2)
    update_output(result)
    

num1_lb = tk.Label(root, text="Enter the first number please : ", font=('calibre', 12, 'bold') )
num2_lb = tk.Label(root, text="Enter the second number please : ", font=('calibre', 12, 'bold'))
lb1 = tk.Label(root, text="Which operation would you like to perform?", font=('Helvetica', 13, 'bold'), fg='brown')
output_lb = tk.Label(root, text="Output", font=('Helvetica', 14, 'bold'), fg='green')

num1_entry = tk.Entry(root, textvariable= num1_var, font=('calibre',10,'normal'))
num2_entry = tk.Entry(root, textvariable= num2_var, font=('calibre',10,'normal'))

add_btn = tk.Button(root, text='+', command=add, activebackground="light cyan", activeforeground="black", relief="raised", bg="cyan", height=2, width=4 )
sub_btn = tk.Button(root, text='-', command=sub, activebackground="light cyan", activeforeground="black", relief="raised", bg="orange", height=2, width=4 )
mul_btn = tk.Button(root, text='x', command=mul, activebackground="light cyan", activeforeground="black", relief="raised", background="blue", height=2, width=4 )
div_btn = tk.Button(root, text='/', command=div, activebackground="red", activeforeground="black", relief="raised", bg="red", height=2, width=4 )

t = tk.Text(root, width=15, height=2,background="light cyan", font=("Times New Roman", 14))


num1_lb.grid(row=0, column=0)
num1_entry.grid(row=0, column=1)
num2_lb.grid(row=1, column=0)
num2_entry.grid(row=1, column=1)

lb1.grid(column=1)

add_btn.grid(row=3,column=0)
sub_btn.grid(row=3,column=1)
mul_btn.grid(row=4,column=0)
div_btn.grid(row=4,column=1)

output_lb.grid(row=5, column=1)
t.grid(row=6,column=1)

root.mainloop()