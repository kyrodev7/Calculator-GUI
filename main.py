import tkinter as tk

def add_numbers():
    # Get the numbers from the entry boxes
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Add them
    result = num1 + num2

    # Show the result
    result_label.config(text=f"Result: {result}")

def substract_numbers():
    # Get the numbers from the entry boxes
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Add them
    result = num1 - num2

    # Show the result
    result_label.config(text=f"Result: {result}")

def multiply_numbers():
    # Get the numbers from the entry boxes
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Add them
    result = num1 * num2

    # Show the result
    result_label.config(text=f"Result: {result}")

def divide_numbers():
    # Get the numbers from the entry boxes
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Add them
    result = num1 / num2

    # Show the result
    result_label.config(text=f"Result: {result}")

def power_numbers():
    # Get the numbers from the entry boxes
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Add them
    result = num1 ** num2

    # Show the result
    result_label.config(text=f"Result: {result}")


def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")



# Window setup
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x200")



# Input fields
entry1 = tk.Entry(window, width=10)
entry1.grid(row=0, column=1, padx=5, pady=5)
                 
entry2 = tk.Entry(window, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)



# Button to add
add_button = tk.Button(window, text="Add", command=add_numbers)
add_button.grid(row=1, column=0, padx=5, pady=5)

# Button to substract
substract_button = tk.Button(window, text="substract", command=substract_numbers)
substract_button.grid(row=1, column=1, padx=5, pady=5)

multiply_button = tk.Button(window, text="multiply", command=multiply_numbers)
multiply_button.grid(row=1, column=2, padx=5, pady=5)

divide_button = tk.Button(window, text="divide", command=divide_numbers)
divide_button.grid(row=1, column=3, padx=5, pady=5)

power_button = tk.Button(window, text="power", command=power_numbers)
power_button.grid(row=1, column=4, padx=5, pady=5)


# Label to show result
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=2, column=1, columnspan=2, pady=10)


clear_button = tk.Button(window, text="Clear", command=clear_all)
clear_button.grid(row=3, column=1, columnspan=2, pady=5)


window.mainloop()
