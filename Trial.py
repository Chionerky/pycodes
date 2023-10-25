import tkinter as tk

def calculate_salary():
    exp()
    try:
        salary = int(salary_entry.get())
        total_allowance = int(newTransport + Health + Feeding + Clothing)
        total_deduction = int(dues() + Taxes())
        netpay = int(salary + total_allowance)
        grosspay = int(salary - total_deduction)

        total_allowance_label.config(text=f"Total Allowance is {total_allowance}")
        total_deduction_label.config(text=f"Total Deduction is {total_deduction}")
        netpay_label.config(text=f"Netpay is {netpay}")
        grosspay_label.config(text=f"Grosspay is {grosspay}")
    except ValueError:
        error_label.config(text="Please enter a valid salary")
        
def exp():
    newTransport = salary*0.015
    return(newTransport,)

# Create the main application window
root = tk.Tk()
root.title("Salary Calculator")

# Create and place labels
salary_label = tk.Label(root, text="Enter amount of salary paid:")
salary_label.pack()

total_allowance_label = tk.Label(root, text="")
total_allowance_label.pack()

total_deduction_label = tk.Label(root, text="")
total_deduction_label.pack()

netpay_label = tk.Label(root, text="")
netpay_label.pack()

grosspay_label = tk.Label(root, text="")
grosspay_label.pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

# Create and place entry widget
salary_entry = tk.Entry(root)
salary_entry.pack()

# Create and place calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_salary)
calculate_button.pack()

# Run the Tkinter main loop
root.mainloop()
